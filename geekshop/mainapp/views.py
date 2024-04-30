from django.shortcuts import render
import json


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
    with open("mainapp/fixtures/cards.json", encoding='utf-8') as file:
        cards_data = json.load(file)

    context = {
        'title': 'geekshop - каталог',
        'heading': 'GeekShop',
        'catalog': [
            {'name': 'Новинки'},
            {'name': 'Одежда'},
            {'name': 'Обувь'},
            {'name': 'Аксессуары'},
            {'name': 'Подарки'}
        ],
        'cards': cards_data,
        'footer_copyright': 'Copyright © GeekShop 2024'
    }
    return render(request, 'mainapp/products.html', context)
