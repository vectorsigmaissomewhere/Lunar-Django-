from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from myapp.views import create
from myapp.views import read
from myapp.views import delete
from myapp.views import update

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/',create, name="create"),
    path('read/',read,name="read"),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>/', delete, name='delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

