from django.shortcuts import render
from mainapp.models import ProductCategory, Product


def index(request):
    context = {
        'title': 'geekshop',
        'heading': 'GeekShop Store',
        'paragraph': 'Новые образы и лучшие бренды на GeekShop Store.'
                     ' Бесплатная доставка по всему миру! Аутлет: до -70% Собственный бренд. -20% новым покупателям.',
        'button_text': 'Начать покупки'
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'title': 'geekshop - каталог',
        'heading': 'GeekShop',
        'product_categories': ProductCategory.objects.all(),
        'products': Product.objects.all(),
        'button_text': 'Отправить в корзину',
        'footer_copyright': 'Copyright © GeekShop 2024'
    }
    return render(request, 'mainapp/products.html', context)
