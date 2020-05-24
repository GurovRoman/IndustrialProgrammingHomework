import os
import logging
import time
import unicodedata
import graphyte


from selenium import webdriver
from bs4 import BeautifulSoup

logging.getLogger().setLevel(logging.INFO)


def parse_investing_page(page):
    currency_block = page.find('div', {'id': 'quotes_summary_current_data'})

    value = currency_block.find('span', {'id': 'last_last'}).text
    value = float(value.replace(',', ''))

    return value


GRAPHITE_HOST = 'graphite'

def send_metrics(currencies):
    sender = graphyte.Sender(GRAPHITE_HOST, prefix='currencies')
    for currency in currencies:
        sender.send(currency[0], currency[1])


def parse_url(driver, url):
    

    driver.get(url)
    
    logging.info('Accessed %s ..', url)
    logging.info('Page title: %s', driver.title)
    time.sleep(5)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    metric = parse_investing_page(soup)

    return metric


currencies = {
    'BTC': 'https://www.investing.com/crypto/bitcoin/btc-usd',
    'ETH': 'https://www.investing.com/crypto/ethereum/eth-usd'
}


def main():
    driver = webdriver.Remote(
        command_executor='http://selenium:4444/wd/hub',
        desired_capabilities={'browserName': 'chrome', 'javascriptEnabled': True}
    )

    values = []

    for currency, url in currencies.items():
        value = parse_url(driver, url)
        values.append((currency, value))
    
    driver.quit()

    send_metrics(values)

if __name__ == '__main__':
    main()
