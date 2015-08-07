__author__ = 'dmitry'
# !/usr/bin/env python
# -*- coding: cp1251-*-

"""
    Get USD/RUB course value from http://www.cbr.ru
"""

import urllib.request, urllib.error
from xml.dom import minidom
from sys import exit


def get_xml_data_from_url(url="http://www.cbr.ru/scripts/XML_daily.asp",file_name='/tmp/course_usd_rub.xml'):
    """ Read URL. """
    try:
        page = urllib.request.urlopen(url)
    except urllib.error.URLError as error_text:
        print('{error}. Check internet connections and URL address'.format(
            error=error_text))
        exit()
    html = page.read()
    with open(file_name, "wb") as localFile:
        localFile.write(html)
    page.close()
    return file_name

def get_USDRUB_course_value(input_xml_name=get_xml_data_from_url()):
    output_dict = {}
    doc = minidom.parse(input_xml_name)
    valute_names = doc.getElementsByTagName('Valute')
    date_value = doc.getElementsByTagName('ValCurs')[0]
    check_course_date = date_value.getAttribute('Date')
    for valute_name in valute_names:
        name = valute_name.getElementsByTagName('Name')[0]
        if name.firstChild.data == 'Доллар США':
            course_value = valute_name.getElementsByTagName('Value')[0]
            output_dict['date'] =  check_course_date
            output_dict['course'] = course_value.firstChild.data
    return output_dict

def main():
    """ Write message. """
#    print("please use the function, but do not run as an executable file")
    xml_data = get_USDRUB_course_value()
    print(xml_data)

if __name__ == "__main__":
    exit(main())
