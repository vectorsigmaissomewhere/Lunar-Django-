from django.db import models
from django.contrib.auth.models import User

class Blogs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="blog")

