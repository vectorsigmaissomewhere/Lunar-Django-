from django.http import FileResponse, Http404
from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import FileData, TextData
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
        text = request.POST.get('sometext')
        # checking if the code already exists or not
        somenumber = generate_random_number()
        check_code_object = FileData.objects.filter(code=somenumber)  
        if not check_code_object:
            if not text:
                FileData.objects.create(code=somenumber,ipaddress=ip, file=file)
                messages.success(request, "You have successfully added your file")
                return redirect('/home/')
            if not file:
                TextData.objects.create(code=somenumber,ipaddress=ip, text=text)
                messages.success(request, "You have successfully added your Text")
                return redirect('/home/')
        else:
            messages.success(request,"Code Already exists")
            return HttpResponseRedirect('/home/')            
    return render(request, 'home.html')

def search(request):
    codelists = FileData.objects.all()

    if 'code' in request.GET and request.GET['code']:
        code = request.GET['code']
        codelists = codelists.filter(code__icontains=code)

    return render(request, 'search.html', {'codelists': codelists})

def download_file(request, file_id):
    try:
        file_data = FileData.objects.get(id=file_id)
        return FileResponse(file_data.file.open(), as_attachment=True, filename=file_data.file.name)
    except FileData.DoesNotExist:
        raise Http404("File not found")