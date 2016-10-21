import json
import unittest

from unittest.mock import patch
from scraperator.pages import ResultsPage


class TestResultsPage(unittest.TestCase):
    def setUp(self):
        self.test_results_page = ResultsPage(250000, open('data/product_results.html'))

    def test_get_product_url_list(self):
        expected_result = 7

        scraped_product_list = self.test_results_page.get_product_url_list()
        self.assertEqual(expected_result, len(scraped_product_list), 'Failed to extract the correct number of products')

    def test_get_total_unit_price(self):
        expected_result = 15.1

        total_unit_price = self.test_results_page.get_total_unit_price()
        self.assertEqual(expected_result, total_unit_price, 'Failed to correctly sum the total unit price')

    @patch('scraperator.pages.ResultsPage.get_total_unit_price')
    @patch('scraperator.utils.request_page')
    @patch('scraperator.pages.ResultsPage.get_product_url_list')
    def test_generate_product_details(self, mock_get_product_url_list, mock_request_page, mock_get_total_unit_price):
        mock_get_product_url_list.return_value = ['one', 'two', 'three']
        mock_request_page.side_effect = [{'size': 10000, 'html': open('data/product.html')},
                                          {'size': 20000, 'html': open('data/product.html')},
                                          {'size': 30000, 'html': open('data/product.html')}]
        mock_get_total_unit_price.return_value = 50.0

        json_reponse_str = self.test_results_page.generate_product_details()
        json_response = json.loads(json_reponse_str)
        self.assertEqual(3, len(json_response['results']), 'Failed to parse correct number of products')

if __name__ == '__main__':
    unittest.main()
