from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def task(request):
    return HttpResponse("Hello world")

def show_task(request):
    return HttpResponse('<h1>Sohan is boss</h1>')
