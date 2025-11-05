from django.shortcuts import render
from django.views.generic import TemplateView,FormView,CreateView,UpdateView,DeleteView
from .forms import LoginForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.backends import ModelBackend


class HomeView(TemplateView):
    template_name = "core/index.html"
    
    def get_context_data(self):
        context = super().get_context_data()
        context["user"] = self.request.user
        return context
    

class LoginFormView(FormView):
    form_class = LoginForm
    template_name =  'core/email-login.html'
    success_url = reverse_lazy('home')
    
    
    def form_valid(self, form):
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password"]
        remember_me = form.cleaned_data["remember_me"]    
        user = authenticate(self.request, username=email, password=password)
        if user:
            login(self.request,user)
            if remember_me:
                self.request.session.set_expiry(None)
            else:
                self.request.session.set_expiry(0)
                
            return super().form_valid(form)
        else:
            form.add_error(None,"Email or password is invalid")
            return self.form_invalid(form)