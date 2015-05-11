#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""Загрузка музыкальных композиций из vk.com
 token & user_id можно получить пройдя по ссылке:
 http://api.vkontakte.ru/oauth/authorize?client_id=2223684&scope=audio&redirect_uri=http://api.vk.com/blank.html&display=page&response_type=token
"""

from vkmusic import *
token = 'b1760b3be39894c16cf2b7181b2397b9a416db0e388f8fa1c80594d9261c2bad137ba6d7a9ecbd08a4434'
user_id = '151629380'


def main():
	netstate = check_inet()
	if not netstate:
		print('Проверьте соединение с интернетом и запутстие скрипт снова.')
		sys.exit
	my_doc = vk_connect(token,user_id)	
	get_music(my_doc)

if __name__ == "__main__":
    sys.exit(main())
