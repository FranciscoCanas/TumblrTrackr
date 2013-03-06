from django.http import HttpResponse
<<<<<<< HEAD
from trackr.models import *
=======
from django.db.models import Max
from django.core.exceptions import ObjectDoesNotExist
from trackr.models import *
from models import *
import datetimes

>>>>>>> 5b9021914409f99f0bc68c1939f827a2866d6647

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
<<<<<<< HEAD
	stuff=limit + ' ' + order
	return HttpResponse(stuff)
=======
	if order == "trending":
		try:
			allpost = Post.objects.get(blog_id = blog_name)
			largest_inc = allpost.objects.all().aggregate(
				Max('note_count'-'prev_note_count'))
			allpost.objects.get(largest_inc = 'note_count'-'prev_note_count')
		except ObjectDoesNotExist:
			return HttpResponse(404)
	return HttpResponse(200)
	
	
>>>>>>> 5b9021914409f99f0bc68c1939f827a2866d6647

def get_trends(request):
	''' Send trending data for all blogs.'''
	limit = request.GET['limit']
	order = request.GET['order']
	stuff = ""
	# Fill this here in. With code.
	return HttpResponse(stuff)


