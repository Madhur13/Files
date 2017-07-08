from django import forms
from django.core.validators import MaxLengthValidator,MinLengthValidator

class BankDetailsForm(forms.Form):
    account_name = forms.CharField(max_length=100)
    account_no = forms.IntegerField()
    ifsc = forms.CharField(max_length=15)

class PaytmDetailsForm(forms.Form):
    paytm_name = forms.CharField(max_length=100)
    paytm_no = forms.IntegerField()

class UserSettingsForm(forms.Form):
    email = forms.EmailField()
    phone = forms.CharField(validators=[MaxLengthValidator(10),MinLengthValidator(10)])

class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput())
    new_password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    
