# PropertyFinder
WebScraping Real Estate Websites &amp; Storing in MongoDB Database

Using Scrapy, an amazing framework for webscraping projects.

## Steps for webscraping:
* Install Scrapy
* To start a project use: `scrapy startproject olx_houses`, here replace olx_houses with your chosen name.
* Create a spider(or many)
* To run the crawler use: `scrapy crawl real` (real is the name of the spider)
* To store results in csv files: `scrapy crawl real -o nameoffile.csv`

I stored the results in a MongoDB database just for the hell of it! :stuck_out_tongue_winking_eye:
