from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import User


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/ToDoList/tasks/')
        else:
            # If account doesn't exist we will redirect to register page
            return redirect('/accounts/register/')
    return render(request, 'login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')


def register_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            email = request.POST.get('email')
            password = request.POST.get('password1')
            print(email,password)
            user = User.object.create_user(email=email, password=password)
            user.save()
            return redirect('/')
        return render(request, 'accounts/register.html')
    else:
        return redirect('/')