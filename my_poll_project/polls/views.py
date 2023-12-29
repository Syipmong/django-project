# from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, World!")

def name(request):
    return HttpResponse("My name is Yippee")


