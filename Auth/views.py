from django.shortcuts import render, reverse, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def intro(request):
    return render(request, 'Auth/intro.html')

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            newUser = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1']
            )
            auth.login(request, newUser)
            return redirect('home')

def signin(request):
    if request.method == 'POST':
        next=request.GET.get('next')
        user = auth.authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user is not None:
            auth.login(request, user)
            if next == '':
                return redirect('home')
            else:
                return redirect(next)
        elif next == '':
            return redirect('/')
        else:
            return redirect('/?next=' + next)

def signout(request):
    auth.logout(request)
    return redirect('Auth:intro')
