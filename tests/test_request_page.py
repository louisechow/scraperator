import unittest

from scraperator.utils import request_page


class TestRequestPage(unittest.TestCase):
    def test_valid_request_page(self):
        test_input = 'http://hiring-tests.s3-website-eu-west-1.amazonaws.com/2015_Developer_Scrape/5_products.html'
        result = request_page(test_input)
        self.assertTrue(result, 'Failed to retrieve webpage')

    def test_invalid_request_page(self):
        test_input = 'http://hiring-tests.s3-website-eu-west-1.amazonaws.com/invalid/5_products.html'
        with self.assertRaises(Exception) as e:
            request_page(test_input)
            self.assertEqual('Error: Unable to retrieve webpage', e.exception)

if __name__ == '__main__':
    unittest.main()
