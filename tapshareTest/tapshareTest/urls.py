from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('download/<int:file_id>/', views.download_file, name='download_file'),
    path('read_text/<int:text_id>/', views.read_text, name='read_text'),
    path('download_text/<int:text_id>/', views.download_text, name='download_text'),
    path('search_text/', views.search_text, name='search_text'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
