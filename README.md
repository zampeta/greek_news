# greek_news
Scrape data from the main newspapers in Greece and check whether the text are more prone to the government or to the opposite party.
Python 3

The code run it
scrapy startproject kathimerini
cd kathimerini/kathimerini/spiders
scrapy genspider titles kathimerini.gr
scrapy runspider titles.py