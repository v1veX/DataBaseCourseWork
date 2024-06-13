import os
import django

from parsers import csv_rw
from my_libs.name_reformer import reform_name

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "catalog.settings")
django.setup()

from main.models import Product

file_paths = ['../parsers/toptygin.csv', '../parsers/zalog.csv', '../parsers/poldoma.csv']

counter = 0
for file in file_paths:
    products = csv_rw.read_all(file)
    for item in products:
        unique_name = reform_name(item[0])
        obj = Product(
            name=item[0],
            price=int(item[1]),
            width=int(item[2]),
            thickness=float(item[3]),
            safe_layer=float(item[4]),
            fire_safety=item[5],
            brand=item[6],
            link=item[7],
            photo=item[8],
            unique_name=unique_name
        )

        try:
            existing_product = Product.objects.get(unique_name=unique_name)
            if existing_product.price > obj.price:
                existing_product.price = obj.price
                existing_product.link = obj.link
                existing_product.photo = obj.photo
            if existing_product.fire_safety == '':
                existing_product.fire_safety = obj.fire_safety
            if existing_product.brand == '':
                existing_product.brand = obj.brand

            counter += 1
            existing_product.save()
        except Product.DoesNotExist:
            obj.save()
print(f'Existing products: {counter}')
