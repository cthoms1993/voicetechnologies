from django.shortcuts import render
from .models import Product


# Create your views here.
def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})


def winvoicepro(request):
    return render(request, "winvoicepro.html")


def winvoiceweb(request):
    return render(request, "winvoiceweb.html")


def formstream(request):
    return render(request, "formstream.html")
