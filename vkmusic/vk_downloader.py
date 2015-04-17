#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""Загрузка музыкальных композиций из vk.com"""

from vkmusic import *
token = '480c0474a5e0fa863afe2e49ff3825aa6ff04c9fea4056d258256da79e16fe75664d0a6b98f3523f55092'
user_id = '151629380'


def main():
	netstate = checkInet()
	if not netstate:
		print('Проверьте соединение с интернетом и запутстие скрипт снова.')
		sys.exit
	my_doc = vkConnect(token,user_id)	
	getMusic(my_doc)
main()
