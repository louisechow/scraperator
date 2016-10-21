import re
import requests


def is_valid_url(url):
    """
    Determines if a URL is valid or not

    :param url (str): The URL to validate
    :return (bool): The return value is either True or False
    """
    regex = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    if regex.match(url):
        return True
    return False


def request_page(url):
    """
    Retrieves a webpage and returns the content and size of the page

    :param url (str): The URL of the webpage to retrieve
    :return (dict): The page size in bytes and the page content
    """
    page = {}
    try:
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception('Error: Unable to retrieve webpage')
        else:
            page['size'] = response.headers['Content-Length']
            page['html'] = response.text
            return page
    except requests.ConnectionError as e:
        print('Error: Unable to connect to server')
