#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""Загрузка музыкальных композиций из vk.com
 token & user_id можно получить пройдя по ссылке:
 http://api.vkontakte.ru/oauth/authorize?client_id=2223684&scope=audio&redirect_uri=http://api.vk.com/blank.html&display=page&response_type=token
"""

from vkmusic import check_inet, vk_connect, get_music
from sys import exit
token = '86ce9541d704630bf5a49572a6116cef89728aae6ee84050565afa0b7d9218f254360a3dad23e76a3d677'
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
