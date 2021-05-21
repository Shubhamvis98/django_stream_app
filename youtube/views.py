from django.shortcuts import render
from django.views.generic.base import  View,HttpResponse

# Create your views here.
class Index(View):
    template_name='index.html'
    def get(self,request):
        variableA ='some text here'
        return render(request,self.template_name,{'variableA':variableA})
    def post(self,request):
        return HttpResponse('this is index view. post request')