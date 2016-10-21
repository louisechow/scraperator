SCRAPERATOR
========================

This is a simple tool to scrape data off a Sainsbury search result page.
Give it a Sainsbury search result webpage and it will return to you the following details:

* A list of products with the following details:
   * title
   * size (of accompanying image)
   * unit price
   * description
* The total unit price for all the products on the page

Pre-requisites
--------------
Please make sure you have the following tools installed:
  * Python 3
  * Pip
  * VirtualEnv


Installation
------------
Get the scraperator project from Github

``git clone https://github.com/louisechow/scraperator.git``

Create a separate environment to run scraperator. If you are using virtualenv, you can do this by running the
following commands:

``virtualenv --python python3 env``

``source env/bin/activate``

Once you have your virtual environment set up and you have retrieved the source from github you can install the dependencies
by running the following command from the root directory of the project.

``pip install -r requirements.txt``

This should install the following dependencies:
- BeautifulSoup - Library for parsing HTML
- requests - Library for HTTP
- nose - Library for running tests

Running tests
-------------
You can run the tests from the root directory using

``nosetests tests``

Running Scraperator
-------------------
From the root directory of the project you can run scraperator using the following command

``python scraperator.py``

Enjoy!
------
