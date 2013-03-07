from django.http import HttpResponse
import datetime
import project_vars as pv
import requests
from models import Blog, Post

#################################
# Retrieving the likes for posts:
#################################
def track(request):
	''' Used to manually start the tracking process for testing'''
	blog_name = request.REQUEST.get('blog', '')
	if blog_name:
		# Used for tracking a single blog_name for testing
		response = _request_likes(blog_name)
	else:
		# Used for starting the blog tracking massive batch job thinga
		response = retrieve_all_likes()

	return HttpResponse(response)

def retrieve_all_likes():
    ''' Retrieve a list of liked posts:

    Method: GET api.tumblr.com/v2/blog/{base-hostname}/likes?api_key={key}
    Parameters:
        - api_key: The authentication key we get when we register an app with tumblr.
        - base-hostname: The name of the host we are tracking.
    Reponse: A JSON with:
        - like_posts: An array of post objects.
        - liked_count: Total number of liked posts.'''		

	# For each blog in Blogs:
    for blog in Blog.objects.all():
        # Send AJAX request to tumblr.com to get da likes
        _request_likes(blog)        
    return

def _request_likes(base_blog):
	''' Helper for retreiving likes from tumblr. 
	Given a base blog, makes the request.'''
	response = requests.get(_likes_request_str(base_blog))
	json=response.json()
	ret = json['meta']['status']
	# Check for valid response
	if (ret)==200:
		# Response OK, so parse json for juicy goodness
		_parse_likes_json(base_blog, json)
	else:
		# Response not OK, so pass the error msg back.
		print json
	return (base_blog + ' tracking response:' + str(ret))

def _parse_likes_json(base_blog, likes_json):
	''' Parse the json reply from tumblr, call retrieve_post_details for each post, 
	and add all of the liked posts	to the base_blog's db entry.'''

	return


def _likes_request_str(base_blog):
	''' Returns a string with the request for gettin' likes, baby.'''
	return	pv.tumblr_url + 'blog/' + base_blog + \
			'/likes?api_key=' + pv.api_key 
		
################################
# Retrieving details for posts
################################
def retrieve_post_details(post):
	''' Retrieve details for some post.'''
	# Fill this here in. With code.
	return

def _post_request_str(base_blog, post_id):
	''' Returns a string with the request for gettin' a post.'''
	return	pv.tumblr_url + 'blog/' + base_blog + \
			'/posts?api_key=' + pv.api_key + '&id=' + post_id

