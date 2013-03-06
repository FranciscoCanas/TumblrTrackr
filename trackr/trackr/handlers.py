from django.http import HttpResponse
from trackr.models import *
import datetimes

def AddBlogToTrack(blog_name):
	''' Add a new blog to our tracking list.'''		
	blog = Blog(host_name = blog_name, likes=blank)
	return HttpResponse(200)

def GetBlogTrends(request):
	''' Send trend data for some specific tumblr blog.'''
	stuff = ""
	# Fill this here in. With code.
	return HttpResponse(stuff)

def GetTrends(request):
	''' Send trending data for all blogs.'''
	stuff = ""
	# Fill this here in. With code.
	return HttpResponse(stuff)
