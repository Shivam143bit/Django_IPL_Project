from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def mahi(request):
    return HttpResponse('<h1><marquee>mahi is the best captain.</marquee></h1>')