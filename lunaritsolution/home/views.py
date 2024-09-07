from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth.forms import AuthenticationForm # login form
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .models import Courses,ContactUs, EnrollStudent, QuizQuestion
from django.contrib.auth.decorators import login_required

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

@login_required
def enrolledcourse(request):
    enrollments = EnrollStudent.objects.filter(user=request.user)
    return render(request, 'enrolledcourse.html', {'enrollments': enrollments})

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


# views for contact us 
def contact(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('emailaddress')
        phonenumber = request.POST.get('phonenumber')
        message = request.POST.get('message')
        contactmodel = ContactUs(fullname=fullname, email=email, phonenumber=phonenumber, message=message)
        messages.success(request, 'You have successfully sent the message')
        contactmodel.save()
        return redirect('/home/')
    else:
        messages.success(request, "please try again")
        return redirect('/home/')
    
# when user clicks on enroll course
@login_required
def enroll(request, id):
    course = Courses.objects.get(id=id)
    user = request.user
    enrollment, created = EnrollStudent.objects.get_or_create(user=user, course=course)
    if created:
        messages.success(request, f"You have successfully enrolled in {course.coursename}!")
    else:
        messages.info(request, f"You are already enrolled in {course.coursename}.")
    return redirect('userdashboard')

# This view is used to remove the enrollment 
@login_required
def removeenroll(request, id):
    removeenrollobj = EnrollStudent.objects.get(id=id)
    removeenrollobj.delete()
    messages.success(request, "Successfully removed from the enrollment")
    return redirect('/enrolledcourse/')

@login_required
def watchvideo(request, id):
    try:
        course = Courses.objects.get(id=id)
        coursevideo = course.video 
        coursename = course.coursename
        checkcoursename = course.coursename
    except Courses.DoesNotExist:
        messages.error(request, "Course not found.")
        return redirect('enrolledcourse')
    return render(request, 'watchcourse.html', {'coursevideo': coursevideo, 'coursename': coursename, 'checkcoursename': checkcoursename})

"""
@login_required
def quizsection(request, coursename):
    questions = QuizQuestion.objects.filter(course=coursename)
    return render(request, 'quiz.html', {'questions': questions})
"""

@login_required
def quizsection(request, coursename):
    if request.method == 'POST':
        form_data = request.POST
        answers = {key: value for key, value in form_data.items() if key.startswith('q')}
        useranswerlist = []
        for question, answer in answers.items():
            print(f"{question}: {answer}")
            useranswerlist.append(answer)
        print("=============This is the useranswer list=======")
        print(useranswerlist)
        # trying to get the answer list 
        answersfromdatabase = QuizQuestion.objects.filter(course=coursename)
        print("=============This is the answer from the database=======")
        correct_answers = [question.correct_answer for question in answersfromdatabase]
        print(correct_answers) 
        # Check if the user submitted all the answers or not
        print("=======length of the two answers======")
        print(len(useranswerlist), len(correct_answers))
        if(len(useranswerlist) != len(correct_answers)):
            print("==========Mismatch in the number of answer user sent and the answer in the database====")
            return render(request, 'userdashboard.html')
        # marks is the correct answer the user gets 
        # using zip to process iterator in parallel i,e the answer from the user and answer from the database
        marks = 0
        for useranswer, correct_answer in zip(useranswerlist, correct_answers):
            print(f"Comparing user answer '{useranswer}' with correct answer '{correct_answer}'")
            if useranswer.strip().lower() == correct_answer.strip().lower():
                marks += 1
                print("==========This is the marks========")
                print(marks)  
        print("============This is the marks the user has obtained==========")
        print(marks)
        """
        If the user scores more than 80% he will be eligible for certificate if not 
        he will not be eligible for certificate
        """
        score_in_percentage = (marks/len(useranswerlist))*100
        if score_in_percentage >= 80:
            print("=====You are eligible for certificate=======")
        elif score_in_percentage < 80:
            print("=====You must score more than 80% to be eligible for certificate======")
            messages.info(request,"You must score more than 80% to be eligible for certificate")
        return render(request, 'userdashboard.html')
    questions = QuizQuestion.objects.filter(course=coursename)
    #return render(request, 'quiz.html')
    return render(request, 'quiz.html', {'question': questions})