from django.http import HttpResponse
from django.db.models import Max
import datetime, json
from django.core.exceptions import ObjectDoesNotExist
from trackr.models import *
import tracker

''' Add a new blog to our tracking list.''' 
def add_blog(request):
	blog_name = request.REQUEST['blog'] # Using .REQUEST instead of .POST for testing
	if (Blog.objects.filter(host_name = blog_name).exists() != True):
		b = Blog(host_name = blog_name)
		b.save()
	tracker._request_likes(blog_name)
	return HttpResponse(blog_name)

''' Send trend data for some specific tumblr blog.'''
def get_blog_trends(request, blog_name):
	limit = request.GET.get('limit', 10)
	order = request.GET.get('order', None)
	if order == None:
				return HttpResponse(content="Please specify order",status=404)	
	blog_obj = Blog.objects.get(host_name = blog_name) #Gets a Blog object in 			database with blog_name as host_name
	result = {"trending" : [], 
	        "order": order, 
	        "limit": limit} #Initializes a JSON object to track all posts liked by a blog
	if order == "Trending":
		blog_likes = blog_obj.likes.order_by('-note_inc')[0:limit] #QuerySet of liked posts with most note_count
		for post in blog_likes:
			trending = {"url": post.url,
			            "image": post.image,
			            "text": post.text,
			            "date": '{:%Y-%m-%d %H:%M:%S %Z}'.format(post.date),
			            "last_track": '{:%Y-%m-%d %H:%M:%S} EST'.format(post.last_track),
			            "last_count": post.note_count,
			            "tracking": get_timestamps(post)}
			result["trending"].append(trending)
	elif order == "Recent":
		blog_likes = blog_obj.likes.order_by('-last_track')[0:limit] #QuerySet of liked posts with most recent tracking
		for post in blog_likes:
			trending = {"url": post.url,
			            "image": post.image,
			            "text": post.text,
			            "date": '{:%Y-%m-%d %H:%M:%S %Z}'.format(post.date),
			            "last_track": '{:%Y-%m-%d %H:%M:%S} EST'.format(post.last_track),
			            "last_count": post.note_count,
			            "tracking": get_timestamps(post)}
			result["trending"].append(trending)
	return HttpResponse(content=json.dumps(result), status=200)

def get_timestamps(post):
	'''Return a list of timestamp dictionaries.'''
	lst = []
	for t in Tracking.objects.filter(post = post.id):
		tdict = {"timestamp" : '{:%Y-%m-%d %H:%M:%S} EST'.format(t.timestamp),
		         "sequence" : t.sequence,
		         "increment" : t.increment,
		         "count" : t.count}
		lst.append(tdict)
	return sorted(lst, key=lambda k: k['sequence'], reverse=True) 
	
def get_trends(request):
	''' Send trending data for all blogs.'''
	
	limit = request.GET.get('limit', 10)
	order = request.GET.get('order', None)
	if order == None:
		return HttpResponse(status=404)
	
	result = {"trending" : [], 
	        "order": order, 
	        "limit": limit} #Initializes a JSON object to track all posts liked by a blog
	if order == 'Trending':
		order_by = '-note_inc'
	elif order == 'Recent':
		order_by = '-date'
	else:
		return HttpResponse(status=404)
	posts = Post.objects.all().order_by(order_by)[0:limit]
	for post in posts:
		trending = {"url": post.url,
	                    "text": post.text,
	                    "image": post.image,
	                    "date": '{:%Y-%m-%d %H:%M:%S %Z}'.format(post.date),
	                    "last_track":'{:%Y-%m-%d %H:%M:%S} EST'.format(post.last_track),
	                    "last_count": post.note_count,
	                    "tracking": get_timestamps(post)}
		result["trending"].append(trending)

	return HttpResponse(content=json.dumps(result), status=200)
	
def ping(request):
	return HttpResponse(200);


