#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Загрузка картинок в альбомы vk.com

token & user_id можно получить пройдя по ссылке:
http://api.vkontakte.ru/oauth/authorize?client_id=2223684&scope=photos&redirect_uri=http://api.vk.com/blank.html&display=page&response_type=token
"""
import os

from vkphoto import check_inet, post_photo_to_vk, get_credentials,get_dir_to_download_path, get_photo_from_vk
from sys import exit

def main():
    """Передаем данные для доступа к api и загружаем фотки."""
    netstate = check_inet()
    if not netstate:
        print('Проверьте соединение с интернетом и запутстие скрипт снова.')
        exit()
    token, user_id, aid = get_credentials()
    dir_path = get_dir_to_download_path('/home/dmitry/Downloads/vkphoto/')
#    request = post_photo_to_vk(token, user_id, aid, dir_path)
    request = get_photo_from_vk(user_id, aid)
    if request is -1:
        print('Ошибка во входных параметрах.')
    else:
        print(request)

if __name__ == "__main__":
    exit(main())
