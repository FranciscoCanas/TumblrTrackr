from django.http import HttpResponse
from django.utils.html import strip_tags
from django.core.exceptions import ObjectDoesNotExist
from django.utils.timezone import utc
import datetime
import project_vars as pv
import requests
from models import Blog, Post, Tracking

####################################
## Retrieving the likes for posts ##
####################################


def track(request):
    ''' Used to manually start the tracking process for testing'''
    # This is to ensure that the client doesn't try to track a blog
    # more often than one hour. This might happen if the client discovers
    # the tracker url.
    #delta = datetime.datetime.now().replace(tzinfo=None) - Last_track.timestamp
    #if (delta.total_seconds()/3600) < 1:
        #return HttpResponse(status=404)
    #else:
        #GLOBAL_LAST_TRACK = datetime.datetime.now()
        ## Used for starting the massive blog tracking batch job
    response = retrieve_all_likes()
    return HttpResponse(_response_list_to_str(response))

def retrieve_all_likes():
    '''Retrieve a list of liked posts:

    Method: GET api.tumblr.com/v2/blog/{base-hostname}/likes?api_key={key}
    Parameters:
        - api_key: The authentication key we get when we register an app with tumblr.
        - base-hostname: The name of the host we are tracking.
    Reponse: A JSON with:
        - like_posts: An array of post objects.
        - liked_count: Total number of liked posts.'''      

    response_list = []

    # For each blog in Blogs:
    for blog in Blog.objects.all():
        # Send AJAX request to tumblr.com to get da likes
        response = request_likes(blog.host_name)        
        response_list.append(response)  
            
    return response_list

def request_likes(blog_host_name):
    ''' Retrieve likes from tumblr for the given blog.'''
    # tumblr API request right here:
    response = requests.get(_likes_request_str(blog_host_name))
    json = response.json()    
    ret = json['meta']['status']
    # Check for valid response

    if (ret) == 200:
        # Response OK, so parse json for juicy goodness
        errcode = _parse_likes_json(blog_host_name, json)
        
    return (blog_host_name, ret)

def _parse_likes_json(blog_host_name, likes_json):
    ''' Parse the json reply from tumblr, call retrieve_post_details for each post, 
        and add all of the liked posts  to the blog_host_name's db entry.'''

    # Get the count
    # Necessary? Probably not, but here it is just in case.
    likes_count = likes_json['response']['liked_count']

    # Find the blog in the database, and start updating it:
    # Necessary? Only if we need to modify the blog here.
    # Otherwise we need it in _parse_post_json below so as to 
    # add this particular post to this blog's likes.
    try:
        blog_obj = Blog.objects.get(host_name=blog_host_name)
    except ObjectDoesNotExist:
        return (blog_host_name, 'Blog Does Not Exist')

    # For each post in the 'likes', extract its json object and handle it:
    for liked_post in likes_json['response']['liked_posts']:
        errcode = _parse_post_json(blog_host_name, liked_post)
    
    return (blog_host_name, 200)


def _likes_request_str(blog_host_name):
    ''' Returns a string with the request for gettin' likes, baby. For example:
    http://api.tumblr.com/v2/blog/artgalleryofontario.tumblr.com/likes?api_key=
        UVsuuWUK99CX70DXIKylXXoCVo1QPvYzYPxKzN0GLTVxyd26bx'''

    return  pv.tumblr_url + 'blog/' + blog_host_name + \
            '/likes?api_key=' + pv.api_key 


####################################
## Some helpers for output stuffs ##
####################################      

def _response_to_str(response):
    ''' Takes a response tuple and formats it for english.'''
    return str(response[0]) + ' request got: ' + str(response[1]) + '\n'

def _response_list_to_str(response_list):
    ''' Takes a list of responses and returns a formatted english string.'''
    return ''.join([_response_to_str(response) for response in response_list])
    
                    
        
#################################
## Retrieving details for posts #
#################################

def _parse_post_json(blog_host_name, liked_post_json):
    ''' Takes the json from a post and extracts all its juicy goodness, then
        makes a database entry for it, if necessary.'''
    
    # Example: liked_post_json['post_url'] to get the url
    blog_obj = Blog.objects.get(host_name = blog_host_name)
    post_url = liked_post_json['post_url']
    post_date = convert_date(liked_post_json['date'])
    post_count = liked_post_json['note_count']
    current_datetime = datetime.datetime.now().replace(tzinfo=utc)
 
    # Different posts have different types of text fields.
    text_field = {"text": "body",
                  "chat": "body",
                  "photo": "caption",
                  "link": "description",
                  "quote": "source",
                  "answer": "answer",
                  "audio": "caption",
                  "video": "caption"}
    
    updated_times_tracked = 1
    if (not Post.objects.filter(url = post_url).exists()):
        # Set default image.
        img = "http://www.athgo.org/ablog/wp-content/uploads/2013/02/tumblr_logo.png"
        txt = strip_tags(liked_post_json[text_field[liked_post_json['type']]].encode('utf-8'))
	# Reduce text length if too long.
	if len(txt) > 100:
	    txt = txt[:100] + "..."

        post_obj = Post(url = post_url,
                        date = post_date,
                        last_track = current_datetime,
                        image = img,
                        note_count = post_count,
                        note_inc = 0,
                        text = txt)
        
        post_obj.save()
        blog_obj.likes.add(post_obj)  
	blog_obj.save()
	
    else:
        # update note_count and last_track.
        post_obj = Post.objects.get(url=post_url)
        prev_count = post_obj.note_count
        updated_times_tracked = post_obj.times_tracked + 1
        Post.objects.filter(url=post_url).update(times_tracked = updated_times_tracked, 
                                                 note_inc = post_count - prev_count,
                                                 note_count = post_count,
                                                 last_track = current_datetime)
	post_obj.save()
	
    # Create new tracking object for post.
    tracking = Tracking(post = post_obj,
                        timestamp = current_datetime,
                        sequence = updated_times_tracked)
    tracking.save()
    
    return 0

def _post_request_str(blog_host_name, post_id):
    ''' Returns a string with the request for gettin' a post.
        For example:
        http://api.tumblr.com/v2/blog/artgalleryofontario.tumblr.com/posts?api_key=
        UVsuuWUK99CX70DXIKylXXoCVo1QPvYzYPxKzN0GLTVxyd26bx&id=23'''
    return  pv.tumblr_url + 'blog/' + blog_host_name + \
            '/posts?api_key=' + pv.api_key + '&id=' + post_id

def convert_date(date):
	''' Convert a date in string form into a datetime object. '''
	
	# example date string: "2013-03-13 12:20:00 EST"
	
	return datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S %Z').replace(tzinfo=utc)
