import requests
from bs4 import BeautifulSoup


class MercadoLivre(object):
    def __init__(self):
        self.__web = requests.get("https://lista.mercadolivre.com.br/placa-de-video")

    def captured_sales_collection(self):
        self.__parser()

    def __parser(self):
        self.__web_page_full = BeautifulSoup(self.__web.text, "html.parser")
        products_list = self.__web_page_full.find_all('li', {'class', 'ui-search-layout__item'})
        for p in products_list:
            price = p.find('div', {'class',
                                   'ui-search-price ui-search-price--size-medium ui-search-item__group__element'}).getText()
            name = p.find('div', {'class', 'ui-search-item__group ui-search-item__group--title'}).getText()
            link = p.find('div', {'class', 'ui-search-result__image'}).find('a')['href']
            print(name, price, link)
