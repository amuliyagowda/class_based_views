from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView
from app.forms import *

# Create your views here.


#return string response using function based view
def string_fbv(request):
    return HttpResponse('<h1>string_fbv</h1>')

#return string response using class based view
class string_cbv(View):
    def get(self,request):
        return HttpResponse('<center><h1>string_cbv</h1></center>')
    
#return html page using function based view
def  html_fbv(request):
    return render(request,'html_fbv.html')

#return html page using class based view
class html_cbv(View):
    def get(self,request):
        return render(request,'html_cbv.html')
    
#inserting data using function based view
def insert_fbv(request):
    d={'ESFO':SchoolForm()}
    if request.method=='POST':
        SFDO=SchoolForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('data submitted')
        else:
            return HttpResponse('data invalid')
    return render(request,'insert_fbv.html',d)

#inserting data using class based views
class insert_cbv(View):
    def get(self,request):
        d={'ESFO':SchoolForm()}
        return render(request,'insert_cbv.html',d)

    def post(self,request):
         if request.method=='POST':
            SFDO=SchoolForm(request.POST)
            if SFDO.is_valid():
                SFDO.save()
                return HttpResponse('data submitted')
            else:
                return HttpResponse('data invalid')
            

class template(TemplateView):
    template_name=template.html
         
