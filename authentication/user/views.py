from django.shortcuts import render, redirect
from django.contrib.auth.models import User # imported User model from django.contrib.auth.models
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(username = username, email=email)
        if user.exists():
            messages.info(request, 'username or email already exists')
            return redirect('/register/')
        
        user = User.objects.create(first_name=first_name, last_name=last_name, username=username,email=email,password=password)
        user.set_password(password) # using set_password to hash the password
        user.save()
        messages.info(request, "Your account has been created")
        return redirect('/register/')
    return render(request,'register.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('/login/')
        
        user = User.objects.get(username=username)

        user = authenticate(username=user.username, password=password)
        
        if user is None:
            messages.error(request, 'Invalid Password')
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/home/')
        
    return render(request, 'login.html')

def home(request):
    return render(request,'home.html')
        
def logout_view(request):
    messages.info(request,"You have successfully logged out")
    logout(request)
    return redirect('/login/')

        
