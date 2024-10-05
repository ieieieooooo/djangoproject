from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('приветик')

def home(request):
    return HttpResponse('домашняя страница')

def feedback(request):
    return HttpResponse('отзывы')