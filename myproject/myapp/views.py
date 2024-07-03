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
        messages.add_message(request,messages.INFO, "Your blog has been created")
        return redirect('create')
    
    return render(request, 'create.html')
