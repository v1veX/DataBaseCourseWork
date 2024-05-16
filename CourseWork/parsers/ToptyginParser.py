from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import codecs


def parse_product_page(url):
    # page = codecs.open("page2.html", "r", "utf_8")

    # Подключение к браузеру для получения полной HTML-страницы (Работает!)
    driver = webdriver.Chrome()
    driver.get(url)
    page = driver.page_source
    driver.quit()

    # Парсим страницу
    soup = BeautifulSoup(page, "html.parser")

    name = ""
    price = 0
    width = 0
    thickness = 0
    safe_layer = 0
    fire_safety_class = "Не указан"
    brand = "Не указан"

    # Непосредственно ищем данные
    name = soup.find("h1").text
    price = int(soup.find(class_="product-item-detail-unit-price").find("span").text)
    prop_list = soup.find_all(class_="product-item-detail-properties-item")
    for prop in prop_list:
        prop_name = prop.find(class_="product-item-detail-properties-name").text
        prop_name = prop_name.replace(": ", "")
        if prop_name == "Толщина, мм":
            thickness = float(prop.find(class_="product-item-detail-properties-value").text.replace(",", "."))
        elif prop_name == "Бренд":
            brand = prop.find(class_="product-item-detail-properties-value").text
        elif prop_name == "Защитный слой, мм":
            safe_layer = float(prop.find(class_="product-item-detail-properties-value").text.replace(",", "."))
        elif prop_name == "Ширина, см":
            width = int(prop.find(class_="product-item-detail-properties-value").text)
        elif prop_name == "Класс пожарной опасности":
            fire_safety_class = prop.find(class_="product-item-detail-properties-value").text

    # Вывод для отладки (тут будет запись в csv файл или что-то подобное)
    print(f"Наименование: {name}")
    print(f"Цена: {price} р./пог. м.")
    print(f"Бренд: {brand}")
    print(f"Ширина, см: {width}")
    print(f"Толщина, мм: {thickness}")
    print(f"Толщина защитного слоя, мм: {safe_layer}")
    print(f"Класс пожарной безопасности: {fire_safety_class}")


def parse_all():
    url = "https://polov.net/catalog/commercial/linoleum_emerald_standart_shir_2m/"
    parse_product_page(url)


# parse_all()