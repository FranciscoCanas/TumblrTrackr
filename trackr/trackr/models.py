# Define all the databases needed, each database will be created as
# 'trackr_[class name], ex class Blog will be created as trackr_blog.
from django.db import models
class Blog(models.Model):
    host_name = models.TextField(primary_key=True)
    likes = models.ManyToManyField(Post)

class Post(models.Model):
    url = models.TextField()
    date = models.TextField() # 
    image = models.TextField() # This is a url to the img
    note_count = models.TextField()
    text = models.TextField()
