import configparser
import time
from selenium import webdriver
from BrowserNavigator.browserNavigator import BrowserNavigator
from BrowserNavigator.cookieManager import CookieManager


def main():
    config = configparser.ConfigParser()
    config.read('config.ini')

    print("Loading browser...")
    browser = browser = webdriver.Chrome("/usr/local/bin/chromedriver")

    page = BrowserNavigator(browser)
    page.log_in()

    CookieManager.save_cookies(browser)

    links_company_lyon = page.get_companies_name(
        'https://www.linkedin.com/search/results/companies/?keywords=Lyon')

    print(str(links_company_lyon))

    # at this point it could be used also the scrapy spider web scraper but you need to retrive cookie and send it in
    # request message
    # Scraper(links)

    # or continuing to use selenium to retrive the data from linkedin
    page.retrieve_data(links_company_lyon, 'lyon_companies.xlsx')

    print("Closing browser...")
    browser.close()


if __name__ == '__main__':
    main()
