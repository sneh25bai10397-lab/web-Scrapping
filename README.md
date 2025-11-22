# web-Scrapping

web scraping tool designed to extract data from E commerce website such as  Flipkart. The script is iterated into search result pages, collects data, and exports it to a CSV file for analysis.

## 📋 Features

* **Data Extraction:** Scraped the following details from each page:
    * Product Name
    * Price
    * Product Description (Specifications)
    * Reviews/Ratings
* **Data Export:** I have Compiled data into a structured Pandas DataFrame and saved it as csv file.

## 🛠️ Prerequisites

in order to  run this project i have installed some of the libraries in vs code using pip:

* `pandas`: For Manipulation of data and CSV export.
* `requests`: For HTTP requests to Flipkart.
* `beautifulsoup4`: For parsing HTML content.
* `lxml`: The parser used by BeautifulSoup.

## ⚙️ Installation

1.  ** Download** this repository to your local machine.
2.  **Install the required libraries** using pip. install librariesand run in vs code or cmd prompt in respective machine :

```bash
pip install pandas requests beautifulsoup4 lxml
