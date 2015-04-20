#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""Загрузка музыкальных композиций из vk.com"""
# token & user_id можно получить пройдя по ссылке:
# http://api.vkontakte.ru/oauth/authorize?client_id=2223684&scope=audio&redirect_uri=http://api.vk.com/blank.html&display=page&response_type=token

from vkmusic import *
token = '13c85c54a174c6a994bf63523518fce77fdb34e9e117543f8878e714ba2918d88e8ba7d7a35794669efc1'
user_id = '151629380'


def main():
	netstate = checkInet()
	if not netstate:
		print('Проверьте соединение с интернетом и запутстие скрипт снова.')
		sys.exit
	my_doc = vkConnect(token,user_id)	
	getMusic(my_doc)
main()
