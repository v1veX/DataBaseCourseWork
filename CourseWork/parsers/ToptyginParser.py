from bs4 import BeautifulSoup
from selenium import webdriver
from parsers import csv_rw


def parse_product_page(url, otg: bool = False):
    # Подключение к браузеру для получения полной HTML-страницы (Работает!)
    driver = webdriver.Chrome()
    driver.get(url)
    page = driver.page_source
    driver.quit()

    # Парсим страницу
    soup = BeautifulSoup(page, "html.parser")

    name = None
    price = 0
    width = 0
    thickness = 0
    safe_layer = 0
    fire_safety_class = None
    brand = None
    image_url = None

    # Непосредственно ищем данные
    name = soup.find("h1").text.strip()
    price = int(soup.find(class_="product-item-detail-unit-price").find("span").text)
    prop_list = soup.find_all(class_="product-item-detail-properties-item")
    for prop in prop_list:
        prop_name = prop.find(class_="product-item-detail-properties-name").text
        prop_name = prop_name.replace(": ", "")
        if prop_name == "Толщина, мм":
            thickness = float(prop.find(class_="product-item-detail-properties-value").text.replace(",", "."))
        elif prop_name == "Бренд":
            brand = prop.find(class_="product-item-detail-properties-value").text.strip()
        elif prop_name == "Защитный слой, мм":
            safe_layer = float(prop.find(class_="product-item-detail-properties-value").text.replace(",", "."))
        elif prop_name == "Ширина, см":
            width = int(prop.find(class_="product-item-detail-properties-value").text)
        elif prop_name == "Класс пожарной опасности":
            fire_safety_class = prop.find(class_="product-item-detail-properties-value").text.strip()
    image_url = f"https://polov.net{soup.find(class_="product-item-detail-slider-image").find("img").get("src")}"

    data = [name, price, width, thickness, safe_layer, fire_safety_class, brand, url, image_url]

    # Запись в CSV файл
    # Каждый раз добавляется новая запись. Если вдруг сайт забанит по IP, то уже спарсенные данные останутся
    csv_rw.write('data.csv', data)

    # Вывод для отладки
    if otg:
        print(data)


def parse_catalog(otg: bool = False):
    start_url = 'https://polov.net/catalog/linoleum/?PAGEN_1='
    links = []

    # Парсим ссылки на продукты из каталога
    for i in range(2, 3):
        driver = webdriver.Chrome()
        driver.get(start_url + str(i))
        page = driver.page_source
        driver.quit()

        soup = BeautifulSoup(page, "html.parser")
        link_items = soup.find_all(class_='product-item-image-wrapper')
        for item in link_items:
            link = f"https://polov.net{item.get('href')}"
            links.append(link)

    # Парсим продукты по каждой ссылке
    for link in links:
        parse_product_page(link, otg)


parse_catalog(True)
