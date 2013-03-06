from django.http import HttpResponse
from django.db.models import Max
from django.core.exceptions import ObjectDoesNotExist
from trackr.models import *
from models import *

''' Add a new blog to our tracking list.'''	
def add_blog(request):
	blog_name = request.REQUEST['blog'] # Using .REQUEST instead of .POST for testing
	b = Blog(host_name = blog_name)
	b.save()
	return HttpResponse(blog_name)

''' Send trend data for some specific tumblr blog.'''
def get_blog_trends(request, blog_name):
	limit = request.GET['limit']
	order = request.GET['order']
	if order == "trending":
		try:
			allpost = Post.objects.get(blog_id = blog_name)
			largest_inc = allpost.objects.all().aggregate(
				Max('note_count'-'prev_note_count'))
			allpost.objects.get(largest_inc = 'note_count'-'prev_note_count')
		except ObjectDoesNotExist:
			return HttpResponse(404)
	return HttpResponse(200)
	

def get_trends(request):
	''' Send trending data for all blogs.'''
	limit = request.GET['limit']
	order = request.GET['order']
	stuff = ""
	# Fill this here in. With code.
	return HttpResponse(stuff)


