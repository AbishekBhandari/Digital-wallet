from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoadMoneyForm(forms.Form):
    amount = forms.DecimalField(max_digits=10, decimal_places=2, min_value=1.00)

class TransferMoneyForm(forms.Form):
    recipient = forms.CharField(max_length=150)
    amount = forms.DecimalField(max_digits=10, decimal_places=2, min_value=1.00)