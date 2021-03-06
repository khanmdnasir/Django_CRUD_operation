from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields=['username','email']
        widgets={
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password1':forms.PasswordInput(render_value=True,attrs={'class':'form-control'}),
            'password2':forms.PasswordInput(render_value=True,attrs={'class':'form-control'})
        }