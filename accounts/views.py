from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login , logout, authenticate
from django.contrib.auth.models import User
from .models import *

# Create your views here.

def login_page(request):
    if request.method=='POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            # email = request.POST.get('email')

            user_obj = User.objects.filter(username = username)
            if not user_obj.exists():
                messages.error(request, 'User not found.')
                return redirect('')

            
            
            if user_obj  := authenticate(username = username, password=password):
                login(request, user_obj)
                return redirect('index')

            messages.error(request, 'Wrong Password.')

            return redirect('Login')

        except Exception as e:
            messages.error(request, 'something went wrong')

            return redirect('Login')
    return render(request, 'accounts/login.html')

def register_page(request):
    if request.method =='POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            # email = request.POST.get('email')

            user_obj = User.objects.filter(username = username)
            if user_obj.exists():
                messages.error(request, 'User already exist try to forget Password.')
                return redirect('Register')

            user_obj = User.objects.create(username = username)
            user_obj.set_password(password)
            user_obj.save()

            messages.error(request, 'Account Created Login Plz.')

            return redirect('Login')

        except Exception as e:
            messages.error(request, 'something went wrong')

            return redirect('Register')

    return render(request, 'accounts/register.html')
