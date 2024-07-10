from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Blogs
from django.contrib import messages
from .forms import BlogForm # blogform to add blogs 
from .forms import SignUpForm #     signup form for signup
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout

"""
def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        subtitle = request.POST.get('subtitle') 
        description = request.POST.get('description')
        image = request.FILES.get('image') 
        Blogs.objects.create(title=title, subtitle=subtitle, description=description, image=image)
        # sending a message to the create.html that the blog has been added
        messages.success(request, "Your blog has been created")
        return redirect('create')
    
    return render(request, 'create.html')
"""

# CREATING BLOG USING MODELFORM
def create(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        form.user_id = request.user.id
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.user
            blog.save()
            return redirect('create')
    else:
        form = BlogForm()
    return render(request, 'create.html',{'form':form})

"""
FOR SIGNUP WE HAVE USED SIGNUPFORM INHERITED FROM USERCREATTIONFORM 
FOR LOGIN WE HAVE USED AUTHENITCATIONFORM FROM DJANGO.CONTRIB.AUTH.FORMS
"""

def register(request):
    if request.method == "POST":
        signupform = SignUpForm(request.POST)
        if signupform.is_valid():
            messages.success(request,"Account created successfully")
            signupform.save()
            redirect('/signup/')
    else:
        signupform = SignUpForm()
    return render(request, 'signup.html', {'form':signupform})

def signin(request):
    # if someone is already authenticated i don't need to login
    if not request.user.is_authenticated:
        if request.method == "POST":
            loginform = AuthenticationForm(request=request, data=request.POST)
            if loginform.is_valid():
                uname = loginform.cleaned_data['username']
                upass = loginform.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in successfully !!')
                    return HttpResponseRedirect('/read/')
        else:
            loginform = AuthenticationForm()
        return render(request, 'login.html', {'form': loginform})
    else:
        return HttpResponseRedirect('/read/')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


def read(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            user = request.user
            queryset = Blogs.objects.filter(user=user)
            context = {'blogs': queryset}
            return render(request,'read.html',context)
    else:
        return HttpResponseRedirect('/login/')

def delete(request, id):
    blog = Blogs.objects.get(id=id) 
    blog.delete()
    messages.success(request, "Your blog has been deleted")
    return redirect('read') 

def update(request,id):
    blog = Blogs.objects.get(id=id)
    if request.method == "POST":
        title = request.POST.get('title')
        subtitle = request.POST.get('subtitle')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        blog.title = title
        blog.subtitle = subtitle
        blog.description = description

        if image:
            blog.image = image
        
        blog.save()
        messages.success(request, "Your blog has successfully updated")
        return redirect('read')

    context = {'blogs':blog}
    return render(request, 'update.html', context)
