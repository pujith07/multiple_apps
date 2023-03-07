from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def firstapp2(request):
    return HttpResponse('<h3>function of firstapp2<h3/')
def secondapp2(request):
    return HttpResponse("<h3>function of secondapp2</h3>")