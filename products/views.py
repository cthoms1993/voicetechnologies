from django.shortcuts import render
from .models import DictationProduct, SpeechProduct, SoftwareProduct


# Create your views here.
def dictation_products(request):
    dictationproducts = DictationProduct.objects.all()
    return render(request, "dictation.html", {"dictationproducts": dictationproducts})


def speech_products(request):
    speechproducts = SpeechProduct.objects.all()
    return render(request, "dictation.html", {"speechproducts": speechproducts})


def software_products(request):
    softwareproducts = SoftwareProduct.objects.all()
    return render(request, "dictation.html", {"softwareproducts": softwareproducts})
