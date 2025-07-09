from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the File Upload API 👋<br>Use /upload/ to upload files.")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('', include('upload.urls')),
]
