from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('Прив джанго')

def catalog(request):
    return HttpResponse('Каталог')

def main(request):
    return HttpResponse('Главная страница')
