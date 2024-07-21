from django.db import models
from django.utils import timezone

class FileData(models.Model):
    code = models.CharField(max_length=100)
    ipaddress = models.CharField(max_length=100)
    file = models.FileField(upload_to="filedata")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code

class TextData(models.Model):
    code = models.CharField(max_length=100)
    ipaddress = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code

    