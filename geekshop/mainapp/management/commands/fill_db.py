import json
from django.core.management.base import BaseCommand

from mainapp.models import ProductCategory, Product


def load_from_json(file_name):
    with open(file_name, mode='r', encoding='utf-8') as file:
        return json.load(file)


class Command(BaseCommand):

    def handle(self, *args, **options):
        data = load_from_json('mainapp/fixtures/product_categories.json')
        for el in data:
            fields = el.get('fields')
            fields['id'] = el.get('pk')
            ProductCategory.objects.create(**fields)

        data = load_from_json('mainapp/fixtures/products.json')
        for el in data:
            fields = el.get('fields')
            fields['id'] = el.get('pk')
            category = fields.get('category')
            _category = ProductCategory.objects.get(id=category)
            fields['category'] = _category
            Product.objects.create(**fields)
