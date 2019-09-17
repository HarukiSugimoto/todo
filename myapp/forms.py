from django import forms
from .models import Login, Register

class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = ('mail_address', 'password')

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ('user_name', 'mail_address', 'password')