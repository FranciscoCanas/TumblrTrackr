# Define all the databases needed, each database will be created as
# 'trackr_[class name], ex. class Blog will be created as trackr_blog.

from django.db import models
class Tracking(models.Model):
    timestamp = models.DateField()
    sequence = models.IntegerField()
    increment = models.IntegerField()
    count = models.IntegerField()

class Post(models.Model):
    url = models.TextField()
    date = models.DateField() # 
    last_track = models.DateField()
    image = models.TextField() # This is a url to the img
    note_count = models.IntegerField()
    note_inc = models.IntegerField()
    text = models.TextField()
    tracking = models.OneToOneField(Tracking)
    
    def __unicode__(self):
        return self.url


class Blog(models.Model):
    host_name = models.TextField(primary_key=True)
    likes = models.ManyToManyField(Post)
    timestamp = models.DateTimeField() # Use to determine last track time
    
    def __unicode__(self):
        return self.host_name
