from bs4 import BeautifulSoup
import requests

url = 'https://vladivostok.pol-doma.com/catalog/napolnye_pokrytiya/linoleum/polukommercheskiy_linoleum/47974/'
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

# Вот с этим уже можно работать
