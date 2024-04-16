from django.contrib.auth import get_user_model, authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from giveaway_app.models import Institution, Donation


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

    # Donation.objects.all().distinct('institution').count()

class IndexView(View):
    def get(self, request):
        count_donations = Donation.objects.count()
        count_institution = Institution.objects.count()
        institutions = Institution.objects.all()
        return render(request, 'giveaway_app/index.html', {'count_donations': count_donations, 'count_institution': count_institution, 'institutions': institutions})