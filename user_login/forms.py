from django import forms

class SignupForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    firstname = forms.CharField(max_length=100)
    lastname = forms.CharField(max_length=100)
    referral = forms.CharField(max_length=15, required=False)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())
