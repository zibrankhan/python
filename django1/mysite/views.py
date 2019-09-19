from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def girl_view(request):
    return HttpResponse('<h1> Hello Mashira Welcome to the Khan Family </h1>')

def wwe_view(request):
    return HttpResponse('<h1> Hello bubby welcome to Monday Night Raw </h1>')

def boy_view(request):
    return  HttpResponse('<h1> Hello Zaroon Khan Welcome to the Khan Family </h1>')

