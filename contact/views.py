from django.conf import settings
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import mail_admins


# Create your views here.
def contact(request):
    if request.method == 'POST':
        c = ContactForm(request.POST)
        if c.is_valid():
            name = c.cleaned_data['name']
            sender = c.cleaned_data['email']
            subject = "You have a new contact form from {}:{}".format(name, sender)
            message = "Subject: {}\n\nMessage: {}".format(c.cleaned_data['subject'], c.cleaned_data['message'])
            mail_admins(subject, message)

            c.save()
            messages.add_message(request, messages.INFO, 'Your contact form has been submitted')
            return redirect('contact')
    else:
        c = ContactForm()
    return render(request, 'contact.html', {'form': c, "map_access_token": settings.MAP_ACCESS_TOKEN})
