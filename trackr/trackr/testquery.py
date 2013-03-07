from models import Blog, Post
from django.http import HttpResponse
def testquery(request):
    
    p1=Post(url='boobies', date='', image='', note_count=2, note_inc=165, text='big')
    p1.save()
    p2=Post(url='ilikecouches', date='', image='', note_count=2, note_inc=33, text='sofa')
    p2.save()
    p3=Post(url='foodporn', date='', image='', note_count=2, note_inc=66, text='bbq')
    p3.save()
    p4=Post(url='artandstuff', date='', image='', note_count=2, note_inc=0, text='hipster')
    p4.save()
    
    b=Blog(host_name='MOFOBITCH')
    b.save()
    b.likes.add(p1,p2,p3,p4)
    b2=Blog.objects.get(host_name='MOFOBITCH').likes.order_by('-note_inc')[0:3]
    for e in b2:
        print(e)
    return HttpResponse(200)