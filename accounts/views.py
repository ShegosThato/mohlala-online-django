from django.shortcuts import render
from .models import Customer
from django.urls import reverse_lazy
from .forms import RegisterForm
from django.views.generic import CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

class SignUpView(CreateView):
    template_name = 'registration/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login')


class ProfileView(LoginRequiredMixin, DetailView):
    template_name = 'accounts/profile.html'
    object_context_name = 'customer'
    model = Customer
    login_url = 'login'