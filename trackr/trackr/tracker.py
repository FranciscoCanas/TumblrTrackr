from django.http import HttpResponse
import datetime
import project_vars
import requests
from models import Blog, Post

def track(request):
	''' Used to manually start the tracking process for testing'''
	blog_name = request.REQUEST.get('blog', '')
	if blog_name:
		_request_likes(blog_name)
	else:
		retrieve_likes()

	return HttpResponse(blog_name)

def retrieve_likes():
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
        # Send AJAX request to tumblr.com. 
        _request_likes(blog)        
    return

def _request_likes(base_blog):
    ''' Helper for retreiving likes from tumblr. 
        Given a base blog, makes the request.'''
    
    
    return


def retrieve_post_details(post):
	''' Retrieve details for some post.'''
	# Fill this here in. With code.
	return
