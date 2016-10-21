import unittest

from scraperator.pages import ProductPage
from scraperator.products import Product


class TestProductPage(unittest.TestCase):
    def setUp(self):
        self.test_product_page = ProductPage(120000, open('data/product.html'))

    def test_get_product_title(self):
        expected_result = "Sainsbury's Apricot Ripe & Ready x5"

        scraped_product_title = self.test_product_page.get_product_title()
        self.assertEqual(expected_result, scraped_product_title, 'Failed to extract the product title')

    def test_get_unit_price(self):
        expected_result = 3.50

        scraped_product_unit_price = self.test_product_page.get_price_per_unit()
        self.assertEqual(expected_result, scraped_product_unit_price, 'Failed to extract the product unit price')

    def test_get_description(self):
        expected_result = "Apricots"

        scraped_product_description = self.test_product_page.get_description()
        self.assertEqual(expected_result, scraped_product_description, 'Failed to extract the product unit price')


    def test_get_product_details(self):
        expected_result = Product('Sainsbury\'s Apricot Ripe & Ready x5', '120.0kb', 3.50, 'Apricots')

        scraped_product = self.test_product_page.get_product_details()
        self.assertEqual(expected_result.title, scraped_product.title, 'Failed to extract the product title')
        self.assertEqual(expected_result.size, scraped_product.size, 'Failed to extract the page size')
        self.assertEqual(expected_result.unit_price, scraped_product.unit_price, 'Failed to extract the unit price')
        self.assertEqual(expected_result.description, scraped_product.description, 'Failed to extract the description')

if __name__ == '__main__':
    unittest.main()
