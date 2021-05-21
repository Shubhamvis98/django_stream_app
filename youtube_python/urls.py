
from django.contrib import admin
from django.urls import path
from youtube.views import Index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', Index.as_view())
]
