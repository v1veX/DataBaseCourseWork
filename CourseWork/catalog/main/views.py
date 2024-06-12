from django.shortcuts import render
from .models import Product


def show_main(request):
    products = Product.objects.all()
    data = {
        'products': products
    }
    return render(request, 'main/index.html', data)
