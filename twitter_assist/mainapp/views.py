from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>this is index page</h1>")

def signup(request):
    return HttpResponse("This is Signup page.")
