from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import User

def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == "POST":
        email = request.POST.get('email')
        name = str(request.POST.get('firstname')) + ' ' + str(request.POST.get('lastname'))
        twitterid = request.POST.get('twitterid')
        password = request.POST.get('password')
        user = User(email=email, name=name, twitterid=twitterid, password=password)
        user.save()
        return redirect('index')
    return render(request, 'signup.html')
