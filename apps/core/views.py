from django.shortcuts import render
from apps.products.models import Product


# Create your views here.
def home(request):
    # products = Product.objects.filter(is_featured=True)
    products = Product.objects.all()

    context = {
        'products': products
    }
    return render(request, 'index.html', context)


def contact(request):
    return render(request, 'contact.html')
