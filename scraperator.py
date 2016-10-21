from scraperator.pages import ResultsPage
from scraperator.utils import is_valid_url, request_page

def run():
    page_url = input('Enter the URL of the page to scrape: ')
    if not is_valid_url(page_url):
        print('Error: The URL you supplied is invalid.')
    else:
        sainsbury_page = request_page(page_url)
        sainsbury_page = ResultsPage(sainsbury_page['size'], sainsbury_page['html'])
        print(sainsbury_page.generate_product_details())


if __name__ == "__main__":
    run()
