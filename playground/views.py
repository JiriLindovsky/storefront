from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def say_hello(request):
    #return HttpResponse('Hello boys!')
    #return render(request,'hello.html')
    return render(request, 'hello.html',{'name': 'Yosh'}) 
