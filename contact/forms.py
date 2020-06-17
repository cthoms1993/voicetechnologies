from django import forms
from .models import Contact
from django.template.defaultfilters import slugify


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
