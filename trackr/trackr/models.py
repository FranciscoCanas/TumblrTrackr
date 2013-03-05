# Define all the databases needed, each database will be created as
# 'trackr_[class name], ex class Blog will be created as trackr_blog.
from django.db import models
class Blog(models.Model):
    host_name = models.TextField()