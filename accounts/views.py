from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from .models import *
from shop.models import *


# Create your views here.
def register(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "This User Name is already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "This Email is already registered")
                return redirect('register')

            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=firstname,
                                                last_name=lastname)
                user.save();
                messages.info(request, "Successful")

        else:
            messages.info(request, "Passwords are miss-matched")
            return redirect('register')
    else:
        return render(request, 'register.html')
    return render(request, 'login.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password1']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Not Registered')
            return redirect('register')
    else:
        return render(request, "login.html")
    return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect('/')

