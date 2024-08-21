from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def gambhir(request):
    return HttpResponse('<h1><marquee>Gambhir is the best coach.</marquee></h1>')