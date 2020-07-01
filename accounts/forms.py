from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(
        required=True,
        label='',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Username'
        })
    )
    email = forms.EmailField(
        required=True,
        label='',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Email'
        })
    )
    password1 = forms.CharField(
        required=True,
        label='',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Password'
        })
    )
    password2 = forms.CharField(
        required=True,
        label='',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Re-Enter Password'
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
            raise ValidationError("This email is already coupled to an "
                                  "account.")
        return email

    """Disable help text of UserCreationForm (answer got from: 
    'https://stackoverflow.com/questions/13202845/removing-help-text-from-django-usercreateform'
    & set default autofocus to first_name instead of the default field of 
    username. """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
        self.fields['username'].widget.attrs['autofocus'] = False


class UserLoginForm(forms.Form):
    """User login form with html attributes set via widgets handlers
    for same."""
    username = forms.CharField(
        required=True,
        label='',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Username',
            'autofocus': 'True'
        })
    )
    password = forms.CharField(
        required=True,
        label='',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Password'
        })
    )
