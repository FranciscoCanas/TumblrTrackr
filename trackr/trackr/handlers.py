from django.http import HttpResponse
from trackr.models import *
import datetimes


''' Add a new blog to our tracking list.'''	
def add_blog(request):
	blog_name = request.POST['blog']
	b = Blog(host_name = blog_name)
	b.save()
	return HttpResponse(blog_name)

''' Send trend data for some specific tumblr blog.'''
def get_blog_trends(request, blog_name):
	limit = request.GET['limit']
	order = request.GET['order']
	
	
	return HttpResponse(stuff)

def get_trends(request):
	''' Send trending data for all blogs.'''
	limit = request.GET['limit']
	order = request.GET['order']
	stuff = ""
	# Fill this here in. With code.
	return HttpResponse(stuff


