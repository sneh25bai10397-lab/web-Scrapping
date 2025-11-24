#Web Scrapping 
# E-Commerce website web Scraper

## Overview of the project
python based web scrapping code is built to extract data about mobile phones pricefrom  E-commerce website such as Amazon and Flipkart. It automates the process of navigating through multiple search result pages, collecting key product details, and saving the data into a structured CSV file for further analysis.

## Features
* **Multi-page Scraping:** Iterates through multiple pages of search results automatically.
* **Data Extraction:** Captures four specific data points for each product:
    * Product Name
    * Price
    * Product Description (specific details )
    * Reviews
* **Data Storage:** Exports the scraped data into a clean `csv` file using Pandas.

## Prerequisites
To run this script, you need Python installed along with the following libraries:
* `pandas`
* `requests`
* `beautifulsoup4`
* `lxml` (for parsing)

### Installation
Installed libraries using pip

```bash
pip install pandas requests beautifulsoup4 lxml

df.to_csv("YOUR_PATH_HERE/flipkart_mobiles.csv")

The script operates in the following steps:

Initialization: Sets up empty lists to hold data.

Looping: Iterates through a defined range of pages.

Request: Sends an HTTP GET request to Flipkart.

Parsing: Uses BeautifulSoup to parse the HTML content.

Extraction: Locates specific HTML class names (e.g., KzDlHZ for names, Nx9bqj for prices) to pull text data.

Export: Converts the lists into a Pandas DataFrame and saves to CSV.
