from django.urls import path

from . import views
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
    path('', views.HomeView.as_view(),name='home'),
    # path('contact/', views.ContactFormView.as_view(),name='contact'),
    path('login/', LoginView.as_view(template_name='core/login.html'),name='login'),
    path('login-email/', views.LoginFormView.as_view(),name='login-email'),
    path('logout/', LogoutView.as_view(),name='logout')
    
    
]
