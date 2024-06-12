import os
import django
from parsers import csv_rw

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "catalog.settings")
django.setup()

from main.models import Product

file_path = '../parsers/toptygin.csv'
products = csv_rw.read_all(file_path)
for item in products:
    obj = Product(
        name=item[0],
        price=item[1],
        width=item[2],
        thickness=item[3],
        safe_layer=item[4],
        fire_safety=item[5],
        brand=item[6],
        link=item[7],
        photo=item[8]
    )
    obj.save()
