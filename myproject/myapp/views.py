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
    if request.user.is_authenticated:
        if request.method == "POST":
            form = BlogForm(request.POST, request.FILES)
            form.user_id = request.user.id
            if form.is_valid():
                blog = form.save(commit=False)
                blog.user = request.user
                blog.save()
                messages.success(request, "Your Blog has been created")
                return redirect('create')
        else:
            form = BlogForm()
        return render(request, 'create.html',{'form':form})
    else:
        return redirect('login')

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
            # queryset = Blogs.objects.filter(user=user) # fetch the data of the current user 
            queryset = Blogs.objects.all() 
            context = {'blogs': queryset}
            return render(request,'read.html',context)
    else:
        return HttpResponseRedirect('/login/')

def delete(request, id):
    if request.user.is_authenticated:
        blog_id = Blogs.objects.get(id=id)
        user_id = blog_id.user_id
        if request.user.id == user_id: # this statement will not let your delete other people's blog
            blog = Blogs.objects.get(id=id) 
            blog.delete()
            messages.success(request, "Your blog has been deleted")
            return redirect('read') 
        else:
            messages.success(request,"Sorry, You cannot delete other user blog")
            return redirect('read')
    else:
        return HttpResponseRedirect('/login/')

def update(request,id):
    if request.user.is_authenticated:
        blog_id = Blogs.objects.get(id=id)
        user_id = blog_id.user_id
        if request.user.id == user_id: # this statement will not let you update other people's blog 
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
        else:
            messages.success(request, "Sorry, You cannot update other user blog")
            return redirect('read')
    else:
        return redirect('login')
