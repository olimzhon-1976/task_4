# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib import messages
from .forms import LoginForm


def index(request):
    context = {
        'title': 'ПРИВЕТ',
    }
    return render(request, "forms/welcome.html", context=context)
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_superuser:
                    return render(request, 'forms/welcome.html', {'level': 'Администратор'}) # login:admin1, password:1234
                else:
                    return render(request, 'forms/welcome.html', {'level': 'Пользователь'}) # login:User1, password:password1user1
            else:
                messages.error(request, 'Неправильный логин или пароль')
        else:
            messages.error(request, 'Неправильный логин или пароль')
    else:
        form = LoginForm()
    return render(request, 'forms/login.html', {'form': form})
