
from django.contrib import admin
from django.urls import path
from youtube.views import Index, NewVideo


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', Index.as_view()),
    path('new_video/', NewVideo.as_view())

]
