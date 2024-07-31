from django.contrib import admin
from django.urls import path
from home.views import home, course, specificcourse, userdashboard, enrolledcourse, certificate, user_login, allCourse, user_logout, contact
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home,name="home"),
    path('course/',course, name='course'),
    path('specificcourse/<int:id>/', specificcourse, name='specificcourse'),
    path('userdashboard/',userdashboard, name='userdashboard'),
    path('enrolledcourse/',enrolledcourse, name='enrolledcourse'),
    path('certificate/', certificate, name='certificate'),
    path('login/',user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('allcourse/',allCourse, name='allcourse'),
    path('contactform/', contact, name='contactform'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
