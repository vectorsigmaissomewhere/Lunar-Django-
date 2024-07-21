from django.http import FileResponse, HttpResponse, Http404
from django.shortcuts import get_object_or_404, render, redirect, HttpResponseRedirect
from .models import FileData, TextData
import random
from django.http import HttpResponse
from django.contrib import messages

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
        somenumber = generate_random_number()
        check_code_object = FileData.objects.filter(code=somenumber)  
        if not check_code_object:
            if not text:
                FileData.objects.create(code=somenumber,ipaddress=ip, file=file)
                messages.success(request, "You have successfully added your file")
                return redirect('/home/')
            if not file:
                TextData.objects.create(code=somenumber,ipaddress=ip, text=text)
                messages.success(request, "You have successfully added your text")
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

def read_text(request, text_id):
    text_data = get_object_or_404(TextData, code=text_id)
    return render(request, 'read_text.html', {'text_data': text_data})

def search_text(request):
    query = request.GET.get('query', '')
    text_list = TextData.objects.all()
    
    if query:
        text_list = text_list.filter(text__icontains=query)

    return render(request, 'text_search.html', {'text_list': text_list, 'query': query})


def download_text(request, text_id):
    text_data = get_object_or_404(TextData, id=text_id)
    response = HttpResponse(text_data.text, content_type='text/plain')
    response['Content-Disposition'] = f'attachment; filename={text_data.code}.txt'
    return response