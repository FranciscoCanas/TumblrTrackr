from django.http import HttpResponse
import datetime
import project_vars

def RetrieveLikes(request):
	''' Retrieve a list of liked posts:

    Method: GET api.tumblr.com/v2/blog/{base-hostname}/likes?api_key={key}
    Parameters:
        - api_key: The authentication key we get when we register an app with tumblr.
        - base-hostname: The name of the host we’re tracking.
    Reponse: A JSON with:
        - like_posts: An array of post objects.
        - liked_count: Total number of liked posts.
    '''		

	# For each blog in Blogs:
    # Send AJAX request to tumblr.com. 
    return


def RetrievePostDetails(request):
	''' Retrieve details for some post.'''
	# Fill this here in. With code.
	return
