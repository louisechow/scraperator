SCRAPERATOR
========================

This is a simple tool to scrape data off a Sainsbury search result page.
Give it a Sainsbury search result webpage and it will return to you the following details:

* A list of products with the following details:
** title
** size (of accompanying image)
** unit price
** description
* The total unit price for all the products on the page

Installation
------------
Scraperator uses Python3. Please install Python3 if you do not have it already

It is recommended that you set up an seperate environment to run scraperator. You can do this by creating a new virtualenv
environment

```
virtualenv --python python3 env
source env/bin/activate
```

Once you have your virtual environment set up and you have retrieved the source from github you can install the dependencies
using the following commands

```
cd scraperator
pip install -r requirements.txt
```

Running tests
-------------
You can run the tests from the root directory using
```
nosetests tests
```

Running Scraperator
-------------------
From the root directory of the project you can run scraperator using the following command
```
python scraperator.py
```



