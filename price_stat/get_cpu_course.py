__author__ = 'dmitry'
# !/usr/bin/env python
# -*- coding: cp1251-*-

"""
    Get cpu price from dns and technopoint.
    sudo pip-3.3 install beautifulsoup4
"""

import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
from sys import exit


def get_html_data_from_url(url="http://technopoint.ru/catalog/2123/processory"):
    """ Read HTML data from URL. """
    try:
        html_page = urllib.request.urlopen(url)
    except urllib.error.URLError as error_text:
        print('{error}.\n Check internet connections and URL address'.format(
            error=error_text))
        exit()
    html = html_page.read()
    return html

def get_products_dict_from_html(html):
    soup = BeautifulSoup(html, 'lxml')
    products_dict = {}
    products_table = soup.find('table', class_='table table-bordered')
    product_count = 0
    for row in products_table.find_all('tr'):
        product = row.find('td', class_='info')
        price = row.find('div', class_='inline')
        try:
            products_dict[product_count] = (product.a.text,price.span.text)
            product_count += 1
        except:
            pass
    return products_dict

def main():
    """ Write message. """
    print("please use the function, but do not run as an executable file")

if __name__ == "__main__":
    exit(main())
