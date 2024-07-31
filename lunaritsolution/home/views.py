from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth.forms import AuthenticationForm # login form
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .models import Courses

def home(request):
    return render(request,'home.html')

def course(request):
    courses = Courses.objects.all()
    return render(request, 'course.html', {'courses':courses})

def specificcourse(request,id):
    onecourse = Courses.objects.get(id=id)
    return render(request, 'specificcourse.html',{'onecourse':onecourse})

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
    
def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully !!')
    return redirect('home')


"""
    # Fetch all MusicalEvent objects
    musical_events = MusicalEvent.objects.all()
    # searching for specific district
    if 'district' in request.GET:
        district = request.GET['district']
        musical_events = musical_events.filter(district__icontains=district)    
    return render(request, 'index.html', {'musical_events': musical_events})

"""


