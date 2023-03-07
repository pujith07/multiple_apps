from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def firstapp1(request):
    return HttpResponse('<h1> function of firstapp1')
def secondapp1(request):
    return HttpResponse('<h1> function of secondapp1')
