from django.db import models

class FileData(models.Model):
    code = models.CharField(max_length=100)
    ipaddress = models.CharField(max_length=100)
    file = models.FileField(upload_to="filedata")

    def __str__(self):
        return self.code
    
class TextData(models.Model):
    code = models.CharField(max_length=100)
    ipaddress = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.code
    