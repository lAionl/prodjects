#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Загрузка музыкальных композиций из vk.com

token & user_id можно получить пройдя по ссылке:
http://api.vkontakte.ru/oauth/authorize?client_id=2223684&scope=audio&redirect_uri=http://api.vk.com/blank.html&display=page&response_type=token
"""

from vkmusic import check_inet, vk_connect, get_music, get_credentials
from sys import exit

def main():
    """Передаем данные для доступа к api и получаем список музыки"""

    netstate = check_inet()
    if not netstate:
        print('Проверьте соединение с интернетом и запутстие скрипт снова.')
        exit()
    token, user_id = get_credentials()
    my_doc = vk_connect(token, user_id)
    get_music(doc = my_doc, dir_to_download_path = '/home/dmitry/Downloads/vkmusic/')

if __name__ == "__main__":
    exit(main())
