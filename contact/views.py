from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages


# Create your views here.
def contact(request):
    if request.method == 'POST':
        c = ContactForm(request.POST)
        if c.is_valid():
            c.save()
            messages.add_message(request, messages.INFO, 'Your contact form has been submitted')
            return redirect('contact')
    else:
        c = ContactForm()
    return render(request, 'contact.html', {'form': c})
