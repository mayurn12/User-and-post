from django.shortcuts import render,redirect
from .forms import CreateUser
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy

# Create your views here.

class HomePage(TemplateView):
    template_name = 'users/base.html'

class CreateViewUser(SuccessMessageMixin,CreateView):
    form_class = CreateUser
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'
    success_message = 'User created successfully'




