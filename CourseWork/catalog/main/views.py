from django.shortcuts import render
from django.db.models import Q
from .models import Product


def show_main(request):
    brand_list = Product.objects.values_list('brand', flat=True).distinct()
    width_list = Product.objects.values_list('width', flat=True).distinct()
    thickness_list = Product.objects.values_list('thickness', flat=True).distinct()

    # Получаем значения запросов
    sort_request = request.GET.get('sort')
    brand_request = request.GET.get('brand')
    width_request = request.GET.get('width')
    thickness_request = request.GET.get('thickness')

    # Берем все данные из БД
    products = Product.objects.all()

    # Фильтруем по бренду, если есть такой запрос
    if brand_request is not None and brand_request != '':
        products = products.filter(brand__icontains=brand_request)
    # Фильтруем по ширине, если есть такой запрос
    if width_request is not None and width_request != '':
        width_request = int(width_request)
        products = products.filter(width=width_request)
    else:
        width_request = 0
    # Фильтруем по толщине, если есть такой запрос
    if thickness_request is not None and thickness_request != '':
        thickness_request = float(thickness_request.replace(',', '.'))
        products = products.filter(thickness=thickness_request)
    else:
        thickness_request = -1.0

    # Сортируем данные, если на то есть запрос
    if sort_request is not None and sort_request != '':
        products = products.order_by(sort_request)

    data = {
        'products': products,
        'brands': brand_list.order_by('brand'),
        'widths': width_list.order_by('width'),
        'thicknesses': thickness_list.order_by('thickness'),
        'sort_request': sort_request,
        'brand_request': brand_request,
        'width_request': width_request,
        'thickness_request': thickness_request,
        'products_length': len(products)
    }
    return render(request, 'main/index.html', data)
