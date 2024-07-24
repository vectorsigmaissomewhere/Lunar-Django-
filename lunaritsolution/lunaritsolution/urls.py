from django.contrib import admin
from django.urls import path
from home.views import home, course, specificcourse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home,name="home"),
    path('course/',course, name='course'),
    path('specificcourse/',specificcourse, name='specificcourse')
]
