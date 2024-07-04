from django.db import models

class Blogs(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="blog")
