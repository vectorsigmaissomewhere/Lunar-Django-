from django.contrib import admin
from django.urls import path
from user.views import register
from user.views import login_view
from user.views import home
from user.views import logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register, name="register"),
    path('login/',login_view,name="login"),
    path('home/', home,name="home"),
    path('logout/',logout_view,name="logout")
]
