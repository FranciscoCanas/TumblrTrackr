from django.http import HttpResponse
import datetime
from project_vars import *
from models import *

def RetrieveLikes():
    ''' Retrieve a list of liked posts:

    Method: GET api.tumblr.com/v2/blog/{base-hostname}/likes?api_key={key}
    Parameters:
        - api_key: The authentication key we get when we register an app with tumblr.
        - base-hostname: The name of the host we are tracking.
    Reponse: A JSON with:
        - like_posts: An array of post objects.
        - liked_count: Total number of liked posts.'''		

	# For each blog in Blogs:
    for blog in Blogs.objects.all():
        # Send AJAX request to tumblr.com. 
        _requestLikes(base_blog)        
    return

def _requestLikes(base_blog):
    ''' Helper for retreiving likes from tumblr. 
        Given a base blog, makes the request.'''
    
    
    return


def RetrievePostDetails(post):
	''' Retrieve details for some post.'''
	# Fill this here in. With code.
	return
