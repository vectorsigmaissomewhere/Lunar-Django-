from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm # login form
from django.contrib import messages
from django.contrib.auth import login, authenticate

def home(request):
    return render(request,'home.html')

def course(request):
    return render(request, 'course.html')

def specificcourse(request):
    return render(request, 'specificcourse.html')

def userdashboard(request):
    return render(request, 'userdashboard.html')

def enrolledcourse(request):
    return render(request, 'enrolledcourse.html')

def certificate(request):
    return render(request, 'certificate.html')

def allCourse(request):
    return render(request, 'allcourses.html')

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in successfully !!')
                    return HttpResponseRedirect('/home/')
        else:
            fm = AuthenticationForm()
        return render(request, 'userlogin.html',{'form':fm})
    else:
        return HttpResponseRedirect('/home/')



