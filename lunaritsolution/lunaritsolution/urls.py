from django.contrib import admin
from django.urls import path
from home.views import home, course, specificcourse, userdashboard, enrolledcourse, certificate, user_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home,name="home"),
    path('course/',course, name='course'),
    path('specificcourse/',specificcourse, name='specificcourse'),
    path('userdashboard/',userdashboard, name='userdashboard'),
    path('enrolledcourse/',enrolledcourse, name='enrolledcourse'),
    path('certificate/', certificate, name='certificate'),
    path('login/',user_login, name='login'),
]
