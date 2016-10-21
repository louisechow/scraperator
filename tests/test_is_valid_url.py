import unittest

from scraperator.utils import is_valid_url


class TestIsValidUrl(unittest.TestCase):
    def test_valid_url(self):
        test_input = 'http://hiring-tests.s3-website-eu-west-1.amazonaws.com/2015_Developer_Scrape/5_products.html'
        result = is_valid_url(test_input)
        self.assertEqual(True, result, 'Failed to recognise valid URL')

    def test_invalid_url(self):
        test_input = 'not a real URL'
        result = is_valid_url(test_input)
        self.assertEqual(False, result, 'Failed to recognise invalid URL')


if __name__ == '__main__':
    unittest.main()