from models import Blog, Post, Tracking
from django.http import HttpResponse
def testquery(request):
    #creates dummy posts
    t1=Tracking(timestamp='2013-03-13 14:20:00 EST',sequence=1,increment=25,count=430)
    p1=Post(url='boobies', date='', image='', note_count=2, note_inc=165, text='big', last_track='2013-03-13 14:20:00 EST', tracking=t1)
    p1.save()
    
    #p2=Post(url='ilikecouches', date='', image='', note_count=2, note_inc=33, text='sofa', last_track='2013-03-13 14:20:00 EST', tracking=Tracking(timestamp='2013-03-13 13:20:00 EST',sequence=1,increment=15,count=413))
    #p2.save()
    
    #p3=Post(url='foodporn', date='', image='', note_count=2, note_inc=66, text='bbq', last_track='2013-03-13 14:20:00 EST', tracking=Tracking(timestamp='2013-03-13 12:20:00 EST',sequence=1,increment=15,count=470))
    #p3.save()
    
    #p4=Post(url='artandstuff', date='', image='', note_count=2, note_inc=0, text='hipster', last_track='2013-03-13 14:20:00 EST', tracking=Tracking(timestamp='2013-03-13 1:20:00 EST',sequence=1,increment=10,count=4540))
    #p4.save()
    
    #create a blog
    b=Blog(host_name='MOFOBITCH')
    
    b.save()
    #add the dummy posts to the blog's likes field
    b.likes.add(p1,p2,p3,p4)
    #query the blog 'MOFOBITCH' and sort all of its likes field by note_inc in descending
    #order, and return a QuerySet of the top 3 note_inc posts
    b2=Blog.objects.get(host_name='MOFOBITCH').likes.order_by('-note_inc')[0:3]
    for e in b2:
        print(e)
    return HttpResponse(200)