from django import forms


class ContactForm(forms.Form):
    name = forms.CharField()
    phone_number = forms.CharField()
    
    
    
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())