from bs4 import BeautifulSoup
import requests
import time
from parsers import csv_writer


def parse_product_page(url, otg: bool = False, num: int = None):
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
    price = int(soup.find(class_="price_value").text.replace(' ', ''))
    prop_list = soup.find(id="props").find_all('tr')

    for prop in prop_list:
        prop_title = prop.find(class_='char_name').find('span').text.strip()
        if prop_title == 'Толщина,мм':
            thickness = float(prop.find(class_='char_value').find('span').text.strip().replace(',', '.'))
        elif prop_title == 'Толщина защитного слоя,мм':
            safe_layer = float(prop.find(class_='char_value').find('span').text.strip().replace(',', '.'))
        elif prop_title == 'Ширина,м':
            width = int(float(prop.find(class_='char_value').find('span').text.strip().replace(',', '.')) * 100)  # Ширина в см
        elif prop_title == 'Класс пожаробезопасности':
            fire_safety_class = prop.find(class_='char_value').find('span').text.strip()

    if '"' in name:
        brand = name.split('"')[1]  # Извлекаем бренд, т.к. отдельно он нигде не прописан
    name = name.replace('"', '')  # Убираем кавычки (они не нужны)
    price = int(price * width / 100)  # Переводим цену за м2 в цену за погонный метр
    image_url = f'https://vladivostok.pol-doma.com{soup.find(class_="popup_link").get("href")}'

    data = [name, price, width, thickness, safe_layer, fire_safety_class, brand, url, image_url]

    # Запись в CSV файл
    csv_writer.write('poldoma.csv', data)

    # Вывод для отладки
    if otg:
        print(num, data)


def parse_catalog(otg: bool = False):
    start_url = 'https://vladivostok.pol-doma.com/catalog/napolnye_pokrytiya/linoleum/?PAGEN_1='
    count = 1

    for i in range(1, 94):
        links = []
        page = requests.get(start_url + str(i))

        soup = BeautifulSoup(page.content, "html.parser")
        link_items = soup.find_all(class_='image_wrapper_block')
        for item in link_items:
            link = f"https://vladivostok.pol-doma.com{item.find('a').get('href')}"
            links.append(link)

        for link in links:
            parse_product_page(link, otg, count)
            count += 1
            time.sleep(3)  # Защита от бана по IP

        time.sleep(5)  # Защита от бана по IP


parse_catalog(True)
