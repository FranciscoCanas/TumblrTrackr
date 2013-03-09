from models import Blog, Post, Tracking
import datetime
from django.http import HttpResponse
from django.utils.timezone import utc
def testquery(request):
    #creates dummy posts
    p1=Post(url='boobies', date='', last_track=datetime.datetime.utcnow().replace(tzinfo=utc), image='', note_count=2, note_inc=165, text='big')
    p1.save()
    
    
    
    tracking1 = Tracking(post = p1, timestamp=datetime.datetime.utcnow().replace(tzinfo=utc), sequence=0, increment=0, count=0)
    tracking1.save()
    print(tracking1.post.url)
    
   
    #p2=Post(url='ilikecouches', date='', image='', note_count=2, note_inc=33, text='sofa')
    #p2.save()
    #p3=Post(url='foodporn', date='', image='', note_count=2, note_inc=66, text='bbq')
    #p3.save()
    #p4=Post(url='artandstuff', date='', image='', note_count=2, note_inc=0, text='hipster')
    #p4.save()
    
    #create a blog
    b=Blog(host_name='MOFOBITCH', timestamp = datetime.datetime.utcnow().replace(tzinfo=utc))
    b.save()
    #add the dummy posts to the blog's likes field
    #b.likes.add(p1,p2,p3,p4)
    #query the blog 'MOFOBITCH' and sort all of its likes field by note_inc in descending
    #order, and return a QuerySet of the top 3 note_inc posts
    #b2=Blog.objects.get(host_name='MOFOBITCH').likes.order_by('-note_inc')[0:3]
    #for e in b2:
        #print(e)
    return HttpResponse(200)