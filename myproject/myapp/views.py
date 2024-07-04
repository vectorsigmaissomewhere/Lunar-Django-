from django.shortcuts import render, redirect
from .models import Blogs
from django.contrib import messages

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

def read(request):
    if request.method == "GET":
        queryset = Blogs.objects.all()
        context = {'blogs': queryset}
        return render(request,'read.html',context)
    
    return render(request,'read.html')

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
