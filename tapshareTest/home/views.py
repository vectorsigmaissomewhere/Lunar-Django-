from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import FileData
import random
from django.contrib import messages

"""This function generates a random 5 digit number"""
def generate_random_number():
    n = 5
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return random.randint(range_start, range_end)

def home(request):
    if request.method == "POST":
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        
        file = request.FILES.get('filename')  
        # checking if the code already exists or not
        somenumber = generate_random_number()
        check_code_object = FileData.objects.filter(code=somenumber)  
        if not check_code_object:
            FileData.objects.create(code=somenumber,ipaddress=ip, file=file)
            return redirect('/home/')
        else:
            messages.success(request,"Code Already exists")
            return HttpResponseRedirect('/home/')            
    return render(request, 'home.html')

def read_code_data(request,code):
    if request.method == "POST":
        check_code_object = FileData.objects.get(code=code)
        context = {'somefiles': check_code_object}
        return render(request,'home.html',context)
    return render(request, "home.html")


