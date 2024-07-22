from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.

# SingUp's function 
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, 'Passwords do not match.')
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken.')
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
            return redirect('signup')

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()

        user = authenticate(username=username, password=password1)
        auth_login(request, user)
        messages.success(request, 'Signup successful! You are now logged in.')
        return redirect('home')

    return render(request, 'signup.html')

# SingIn's function 
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('home')  # Change 'home' to your desired redirect URL
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')

# Home page
@login_required
def home(request):
    return render(request, "home.html")

# Logout funtion
def custom_logout_view(request):
    logout(request)
    return redirect('login') 


