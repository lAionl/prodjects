#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""Загрузка музыкальных композиций из vk.com"""
# token & user_id можно получить пройдя по ссылке:
# http://api.vkontakte.ru/oauth/authorize?client_id=2223684&scope=audio&redirect_uri=http://api.vk.com/blank.html&display=page&response_type=token

from vkmusic import *
token = '61a4045f0ddd770e3675639bd8cd2c6a4f8f96825cf4e0161abe6d99fd78389d63da2f191514e8c1722a8'
user_id = '151629380'


def main():
	netstate = check_inet()
	if not netstate:
		print('Проверьте соединение с интернетом и запутстие скрипт снова.')
		sys.exit
	my_doc = vk_connect(token,user_id)	
	get_music(my_doc)
main()
