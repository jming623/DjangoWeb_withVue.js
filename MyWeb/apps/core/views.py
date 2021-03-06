from unicodedata import category
from django.shortcuts import render

from apps.store.models import Product

def frontpage(request):
    # products = Product.objects.all()
    products = Product.objects.filter(is_featured=True)

    context = {
        'products' :products
    }

    return render(request, 'frontpage.html', context)

def contactpage(request):
    return render(request, 'contact.html')

def aboutpage(request): 
    return render(request, 'about.html')

