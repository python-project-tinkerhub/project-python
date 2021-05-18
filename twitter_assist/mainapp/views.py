from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import User

def index(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(email=email).count()!=0:
            if User.objects.filter(email=email, password=password).count() ==1:
                request.session['email'] = email
                return redirect('dashboard')
            return render(request, 'index.html', {'error': 'wpwd'})
        return render(request, 'index.html', {'error': 'wemail'})
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

def dashboard(request):
    return render(request, 'dashboard.html')

def logout(request):
    try:
        del request.session['email']
    except:
        pass
    return redirect('index')
