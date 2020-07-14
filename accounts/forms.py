from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(
        required=True,
        label='Username',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        })
    )
    email = forms.EmailField(
        required=True,
        label='Email',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
        })
    )
    password1 = forms.CharField(
        required=True,
        label='Enter Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
        })
    )
    password2 = forms.CharField(
        required=True,
        label='Re-enter password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
        })
    )

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise ValidationError("This email is already registered to an"
                                  "account.")
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
        self.fields['username'].widget.attrs['autofocus'] = False


class UserLoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        label='Username:',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'autofocus': 'True',

        })
    )
    password = forms.CharField(
        required=True,
        label='Password:',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',

        })
    )
