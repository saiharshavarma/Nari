from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import Profile
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        mobile = request.POST['mobile']
        password1 = request.POST['password']
        password2 = request.POST['confirm_password']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email ID already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    first_name=first_name, last_name=last_name, username=username, email=email, password=password1)
                user.save()
                profile = Profile.objects.create(user=user, mobile=mobile)
                profile.save()
                return redirect('login')
        else:
            messages.info(request, 'Passwords are not matching')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('register')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')
