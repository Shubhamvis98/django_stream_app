from django.shortcuts import render
from django.views.generic.base import  View,HttpResponse


# Create your views here.
class Index(View):
    template_name='index.html'
    def get(self,request):
        variableA ='title'
        return render(request,self.template_name,{'variableA':variableA})
    def post(self,request):
        return HttpResponse('this is index view. post request')


class NewVideo(View):
    template_name = 'new_video.html'

    def get(self, request):
        variableA = 'new video'
        return render(request, self.template_name, {'variableA': variableA})

    def post(self, request):
        return HttpResponse('this is index view. post request')