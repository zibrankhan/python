from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def date_time_view(request):
    date = datetime.datetime.now()
    s = '<h1> The Current Date and Time is :' + str(date) + '</h1>'
    return HttpResponse(s)

