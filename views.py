from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to Rasduino, where Raspbery pi met Rasduino!")

def about(request):
    return HttpResponse("Here is something about me!")