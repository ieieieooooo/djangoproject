from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('привет')

def django(request):
    return HttpResponse('Django')

def github(request):
    return HttpResponse('github')