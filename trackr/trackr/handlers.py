from django.http import HttpResponse
from django.db.models import Max
import datetime, json
from django.core.exceptions import ObjectDoesNotExist
from trackr.models import *
import requests
import tracker


def add_blog(request):
    ''' Add a new blog to our tracking list.''' 
    blog_name = request.REQUEST['blog'] # Using .REQUEST instead of .POST for testing
    if (not Blog.objects.filter(host_name = blog_name).exists()):
        # We track a blog for the first time as soon as an add blog request
        # is made for that particular blog.
        response = requests.get(tracker._likes_request_str(blog_name))
        if  response.status_code == 404:
            return HttpResponse(content="Not a valid tumblr url",status=404)
        b = Blog(host_name = blog_name,last_track=datetime.datetime.utcnow())
        b.save()
        tracker.request_likes(blog_name)
    return HttpResponse(content=blog_name, status=200)

def get_trends(request, blog_name=None):
    ''' Send trend data for some specific tumblr blog ,
    or all blogs if blog_name=None.'''
    
    limit = request.GET.get('limit', 10)
    # Order must be specified.
    order = request.GET.get('order')
    if order == None:
        return HttpResponse(content="Order not specified.", status=404) 
    
    #Initialize a JSON object that will contain trends.
    post_list = []
    
    if order == "Trending":
        orderby = 'note_inc'
    elif order == "Recent":
        orderby = 'date'
    else:
        return HttpResponse(content=order + " is not a valid order.", status=404)   
    
    if blog_name:
        # Get liked posts for this specific blog.
        try:
            blog_obj = Blog.objects.get(host_name = blog_name)
            
        except ObjectDoesNotExist:
            return HttpResponse(content="Requested blog is not being tracked", status=404);
            
        posts = blog_obj.likes.all()
    else:   
        # Get liked posts for all blogs.
        posts = Post.objects.all()
    
    # QuerySet of liked posts with sorted by either '-note_inc' or 'date',
    # depending on order parameter.
    for post in posts:
        p = {"url": post.url,
             "image": post.image,
             "text": post.text,
             "date": '{:%Y-%m-%d %H:%M:%S %Z}'.format(post.date),
             "last_track": '{:%Y-%m-%d %H:%M:%S %Z}'.format(post.last_track),
             "last_count": post.note_count,
             "tracking": get_timestamps(post)}
        post_list.append(p)
    
    if order == "Trending":
        post_list = sorted(post_list, key=lambda k: k['tracking'][0]['increment'], reverse=True)
    elif order == "Recent":
        post_list = sorted(post_list, key=lambda k: k['date'], reverse=True)
    post_list = post_list[0:int(limit)]
    result = {order.lower() : post_list, 
            "order": order, 
            "limit": limit}
    return HttpResponse(content=json.dumps(result), status=200)

def get_timestamps(post):
    '''Return a list of timestamp dicts.'''
    
    lst = []
    for t in Tracking.objects.filter(post = post.post_id):
        tdict = {"timestamp" : '{:%Y-%m-%d %H:%M:%S %Z}'.format(t.timestamp),
                 "sequence" : t.sequence,
                 "increment" : t.increment,
                 "count" : t.count}
        lst.append(tdict)
        
    # Return timestamps sorted by descending sequence number
    return sorted(lst, key=lambda k: k['sequence'], reverse=True) 
    
def ping(request):
    return HttpResponse(content="PING!", status=200);


