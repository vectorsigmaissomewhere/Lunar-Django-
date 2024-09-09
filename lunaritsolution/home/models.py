from django.db import models
from django.contrib.auth.models import User

class Courses(models.Model):
    coursename=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to='courseImage/')
    video = models.FileField(upload_to='courseVideo/', default='null')
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

# we are editing enroll student to store the pdf file 
class EnrollStudent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} enrolled in {self.course.coursename}"


class QuizQuestion(models.Model):
    course = models.CharField(max_length=255,null=False, default='unknown course')
    question = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=255, null=False)
    
    def __str__(self):
        return f"{self.question}"

class QuizOption(models.Model):
    question = models.ForeignKey(QuizQuestion, related_name='options', on_delete=models.CASCADE)
    option1 = models.CharField(max_length=255,default='null')
    option2 = models.CharField(max_length=255, default='null')
    option3 = models.CharField(max_length=255, default='null')
    option4 = models.CharField(max_length=255, default='null')

    def __str__(self):
        return f"{self.question}"


# certificate
class Certificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='certificates', default=1)
    pdf = models.FileField(upload_to='certificates/', default='null')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Certificate for {self.user.username}"