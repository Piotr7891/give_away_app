from django.contrib.auth import get_user_model, authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View


class IndexView(View):
    def get(self, request):
        return render(request, 'giveaway_app/index.html')

class LoginView(View):
    def get(self, request):
        return render(request, 'giveaway_app/login.html')

class RegisterView(View):
    def get(self, request):
        return render(request, 'giveaway_app/register.html')

class AddDonationView(View):
    def get(self, request):
        return render(request, 'giveaway_app/form.html')

