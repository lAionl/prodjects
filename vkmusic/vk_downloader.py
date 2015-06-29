#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Загрузка музыкальных композиций из vk.com

token & user_id можно получить пройдя по ссылке:
http://api.vkontakte.ru/oauth/authorize?client_id=2223684&scope=audio&redirect_uri=http://api.vk.com/blank.html&display=page&response_type=token
"""

from vkmusic import check_inet, vk_connect, get_music
from sys import exit
token = '78d3c951de56183ffd42cbb7e4a4e25e828bd499bd7c457f38c749b94f87d96323a27f6107a1f01f558ee'
user_id = '151629380'


def main():
    """Передаем данные для доступа к api и получаем список музыки"""
    netstate = check_inet()
    if not netstate:
        print('Проверьте соединение с интернетом и запутстие скрипт снова.')
        exit()
    my_doc = vk_connect(token, user_id)
    get_music(my_doc)

if __name__ == "__main__":
    exit(main())
