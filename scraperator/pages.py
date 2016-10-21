import json
import re

from bs4 import BeautifulSoup

from scraperator import utils
from scraperator.products import Product


class Webpage:
    """
    Representation of a web page

    Attributes:
        page_size_in_bytes (str): The size of the page
        page_html (str): The content of the page
    """
    def __init__(self, page_size_in_bytes, page_html):
        self.page_size = '{}kb'.format(round(float(page_size_in_bytes) / 1000, 1))
        self.page_source = BeautifulSoup(page_html, 'html.parser')


class ProductPage(Webpage):
    """
    Representation of a Sainsbury product page

    """
    def get_product_title(self):
        """
        Scrapes the HTML to retrieve the product title

        :return (str): Product title
        """
        product_details = self.page_source.find('div', attrs={'class': 'productTitleDescriptionContainer'})
        return product_details.find('h1').contents[0].strip(' \t\n\r')

    def get_price_per_unit(self):
        """
        Scrapes the HTML to retrieve the price per unit

        :return (float) Price per unit:
        """
        product_price = self.page_source.find('p', attrs={'class': 'pricePerUnit'}).contents[0].strip(' \t\n\r')
        return round(float(product_price[1:]), 2)

    def get_description(self):
        """
        Scrapes the HTML to retrieve the description

        :return (str): Product description
        """
        product_description = self.page_source.find('div', attrs={'class': 'productText'})
        return product_description.find('p').contents[0]

    def get_product_details(self):
        """
        Scrapes the details of the product

        :return (Product): The details of the product
        """
        return Product(self.get_product_title(), self.page_size, self.get_price_per_unit(), self.get_description())


class ResultsPage(Webpage):
    """
    Representation of a Sainsbury search results page

    """
    def get_product_url_list(self):
        """
        Scrapes a list of all product pages from the results page

        :return [str]: A list of product page URLS
        """
        product_url_list = []
        products = self.page_source.findAll('div', attrs={'class': 'productInfo'})
        for div in products:
            links = div.findAll('a')
            for a in links:
                product_url_list.append(a['href'])
        return product_url_list

    def get_total_unit_price(self):
        """
        Scrapes the unit price of all products and returns the total

        :return (float): Total unit price of all products
        """
        total_unit_price = 0
        product_prices_html = self.page_source.findAll('p', attrs={'class': 'pricePerUnit'})
        for product_price_html in product_prices_html:
            product_price = product_price_html.contents[0].strip()
            number = re.findall(r"[-+]?\d*\.\d+|[-+]?\d+", product_price)[0]
            total_unit_price += float(number)
        return round(total_unit_price, 2)

    def generate_product_details(self):
        """
        Returns the products details of all products in JSON form

        :return (str): JSON of all products on the page
        """
        results = []
        for product_url in self.get_product_url_list():
            product_content = utils.request_page(product_url)
            product_page = ProductPage(product_content['size'], product_content['html'])
            results.append(product_page.get_product_details().convert_to_json())
        json_output = {}
        json_output['results'] = results
        json_output['total'] = self.get_total_unit_price()
        return json.dumps(json_output)
