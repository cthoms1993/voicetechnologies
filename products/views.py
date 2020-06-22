from django.shortcuts import render
from .models import Product


# Create your views here.
def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})


def win_voice_pro(request):
    return render(request, "winvoicepro.html")


def win_voice_web(request):
    return render(request, "winvoiceweb.html")


def form_stream(request):
    return render(request, "formstream.html")
