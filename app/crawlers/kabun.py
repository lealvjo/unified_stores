import requests
from bs4 import BeautifulSoup


class Kabun(object):
    def __init__(self):
        url = 'https://www.kabum.com.br/hardware/placa-de-video-vga'
        self.__response = requests.get(url)

    def captured_sales_collection(self):
        self.__parser()

    def __parser(self):
        self.__web_page_full = BeautifulSoup(self.__response.text, 'html.parser')
        products_list = self.__web_page_full.select('div[class*="productCard"]')
        for p in products_list:
            name_product = p.find('h2').getText()
            old_price = p.find('span', {'class*', 'oldPriceCard'}).getText()
            current_price = p.find('span', {'class*', 'priceCard'}).getText()
            img_product = [image['src'] for image in p.findAll('img')][0]
            link_product = f"https://www.kabum.com.br{p.find('a')['href']}"
            print(name_product, old_price, current_price, img_product, link_product)
