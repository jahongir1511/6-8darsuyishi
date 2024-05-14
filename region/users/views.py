from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CustomUserForm

class RegisterView(View):
    def get(self, request):
        form = CustomUserForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = CustomUserForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('users:login')
        return render(request, 'register.html', {'form': form})

class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('landing_page')
        return render(request, 'login.html', {'form': form})

class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('landing_page')