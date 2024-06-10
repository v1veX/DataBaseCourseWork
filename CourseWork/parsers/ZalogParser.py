from bs4 import BeautifulSoup
import requests
import time
from my_libs import csv_writer


def parse_product_page(url, otg: bool = False):
    # Получаем HTML-код
    page = requests.get(url)

    # Парсим страницу
    soup = BeautifulSoup(page.content, "html.parser")

    name = None
    price = 0
    width = 0
    thickness = 0
    safe_layer = 0
    fire_safety_class = None
    brand = None
    image_url = None

    # Ищем данные
    name = soup.find("h1").text.strip()
    price = int(soup.find(class_="price_value").text.replace('\xa0', ''))
    prop_list = soup.find_all(class_="properties__item")

    for prop in prop_list:
        prop_title = prop.find(class_='properties__title').text.strip()
        if prop_title == 'Ширина':
            width = prop.find(class_='properties__value').text.strip()
            width = width.replace(',', '.')
            width = width.replace(' ', '')
            width = width.replace('м', '')
            width = int(float(width) * 100)
        elif prop_title == 'Толщина защитного слоя':
            safe_layer = prop.find(class_='properties__value').text.strip()
            safe_layer = safe_layer.replace(',', '.')
            safe_layer = safe_layer.replace(' ', '')
            safe_layer = safe_layer.replace('мм', '')
            safe_layer = float(safe_layer)
        elif prop_title == 'Общая толщина':
            thickness = prop.find(class_='properties__value').text.strip()
            thickness = thickness.replace(',', '.')
            thickness = thickness.replace(' ', '')
            thickness = thickness.replace('мм', '')
            thickness = float(thickness)
        elif prop_title == 'Класс пожарной безопасности':
            fire_safety_class = prop.find(class_='properties__value').text.strip()
        elif prop_title == 'Бренд':
            brand = prop.find(class_='properties__value').text.strip()
    image_url = f"https://zalog-vostok.ru{soup.find(class_="detail-gallery-big__picture").get("src")}"

    data = [name, price, width, thickness, safe_layer, fire_safety_class, brand, url, image_url]

    # Запись в CSV файл
    csv_writer.write('zalog.csv', data)

    # Вывод для отладки
    if otg:
        print(data)


def parse_catalog(otg: bool = False):
    start_url = 'https://zalog-vostok.ru/catalog/napolnye_pokrytiya/linoleum/?PAGEN_1='
    links = []

    # Парсим ссылки на продукты из каталога
    for i in range(1, 10):
        page = requests.get(start_url + str(i))

        soup = BeautifulSoup(page.content, "html.parser")
        link_items = soup.find_all(class_='image_wrapper_block')
        for item in link_items:
            link = f"https://zalog-vostok.ru{item.find('a').get('href')}"
            links.append(link)

        time.sleep(3)  # Защита от бана по IP

    print(len(links))

    # Парсим продукты по каждой ссылке
    for link in links:
        parse_product_page(link, otg)
        time.sleep(3)  # Защита от бана по IP


parse_catalog(True)
