from django.db import models

class Courses(models.Model):
    coursename=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to='courseImage/')
    price=models.IntegerField()

    def str(self):
        return self.coursename

class ContactUs(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    phonenumber = models.CharField(max_length=10)
    message = models.TextField()

    def str(self):
        return self.fullname
    
