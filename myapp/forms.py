from django import forms
from .models import Login, Register, Schedule

class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = ('mail_address', 'password')

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ('user_name', 'mail_address', 'password')

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ('user_name', 'year', 'month', 'date', 'action')