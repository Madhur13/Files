from django import forms

class BankDetailsForm(forms.Form):
    account_name = forms.CharField(max_length=100)
    account_no = forms.IntegerField()
    ifsc = forms.CharField(max_length=15)

class PaytmDetailsForm(forms.Form):
    paytm_name = forms.CharField(max_length=100)
    paytm_no = forms.IntegerField()
