from django.contrib import admin
from .models import Courses, ContactUs, EnrollStudent, QuizQuestion, QuizOption

admin.site.register(Courses)
admin.site.register(ContactUs)
admin.site.register(EnrollStudent)
admin.site.register(QuizQuestion)
admin.site.register(QuizOption)