from django.http import HttpResponse
from django.db.models import Max
from django.core.exceptions import ObjectDoesNotExist
from trackr.models import *
from models import *

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
	if order == "Trending":
		try:
			allpost = Post.objects.get(blog_id = blog_name)
			largest_inc = allpost.objects.all().aggregate(
				Max('note_count'-'prev_note_count'))
			allpost.objects.get(largest_inc = 'note_count'-'prev_note_count')
		except ObjectDoesNotExist:
			return HttpResponse(404)
	return HttpResponse(200)
	
'''Send trends from all blogs that the user is subsribed to'''
def get_trends(request):
	''' Send trending data for all blogs.'''
	limit = request.GET.get('limit', 7)
	order = request.GET['order']
	if order == 'Trending':
		stuff = "Trending"
	elif order == "Recent":
		stuff = "Recent"
	else:
		return HttpResponse(200)
	# Fill this here in. With code.
	return HttpResponse(stuff)


