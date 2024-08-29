from django.db import models
from django.contrib.auth.models import User

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
    
class EnrollStudent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} enrolled in {self.course.coursename}"

