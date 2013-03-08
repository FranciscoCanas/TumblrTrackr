from models import Blog, Post
from django.http import HttpResponse
def testquery(request):
    #creates dummy posts
    p1=Post(url='boobies', date='', image='', note_count=2, note_inc=165, text='big')
    p1.save()
    p2=Post(url='ilikecouches', date='', image='', note_count=2, note_inc=33, text='sofa')
    p2.save()
    p3=Post(url='foodporn', date='', image='', note_count=2, note_inc=66, text='bbq')
    p3.save()
    p4=Post(url='artandstuff', date='', image='', note_count=2, note_inc=0, text='hipster')
    p4.save()
    
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