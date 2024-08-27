from django import forms
from .models import SendMessage
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class ContactForm(forms.ModelForm):
    class Meta:
        model = SendMessage
        fields = '__all__'
        

#for authentication 
class CustomLoginForm(AuthenticationForm):
    pass  # Add custom fields or validation here if needed

#for registration
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
