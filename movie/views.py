from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # return HttpResponse('<h1>Welcome to Home Page </h1>')
    # return render(request,'home.html')
    return render(request,'home.html',{'name':' Sahian Salomé Gutiérrez Ossa'})

def about(request):
     #return HttpResponse('<h1>Welcome to About page </h1>')
     return render(request,'about.html')