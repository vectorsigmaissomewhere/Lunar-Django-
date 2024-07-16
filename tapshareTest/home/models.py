from django.db import models

class FileData(models.Model):
    code = models.CharField(max_length=100)
    ipaddress = models.CharField(max_length=100)
    file = models.FileField(upload_to="filedata")
    
