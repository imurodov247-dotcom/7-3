from django.shortcuts import render
from django.views.generic import TemplateView,FormView,CreateView,UpdateView,DeleteView
from .forms import LoginForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login



class HomeView(TemplateView):
    template_name = "core/index.html"

# class LoginFormView(FormView):
    # form_class = 