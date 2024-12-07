from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Test

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Adresse email")
    is_teacher = forms.BooleanField(required=False, label="Je suis un enseignant")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Cette adresse email est déjà utilisée.")
        return email

class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['title', 'description']
