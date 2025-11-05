from django import forms


class ContactForm(forms.Form):
    name = forms.CharField()
    phone_number = forms.CharField()
    
    
    
class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput())