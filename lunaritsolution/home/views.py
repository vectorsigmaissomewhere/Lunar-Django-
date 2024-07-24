from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def course(request):
    return render(request, 'course.html')

def specificcourse(request):
    return render(request, 'specificcourse.html')