#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""Модуль для работы с музыкой из vk.ru"""

# Для модуля lxml установите пакет python-lxml, а так же
# выполните pip install cssselect
import socket, os, lxml.html, re, urllib.request

# Функция проверки соединения с сетью
def check_inet():
	try:
		socket.gethostbyaddr('www.yandex.ru')
	except socket.gaierror:
		return False
	return True

# Функция подключения к vk и получения списка музыки
def vk_connect(access_token, user_id):
	url = "https://api.vkontakte.ru/method/audio.get.xml?uid=" + user_id + "&access_token=" + access_token
	try:
		page = urllib.request.urlopen(url)
	except urllib.error.URLError as e:
		print(e + '\nПроверьте правильность token для ' + user_id + ',\nтекущее значение = ' + access_token)
		os.exit()
	html = page.read()
	doc = lxml.html.document_fromstring(html)
	return doc

# Функция наполнения массива данными для getTrackInfo
def get_trackinfo(target_info, input_doc):
	outputMas = []
	for values in input_doc.cssselect(target_info):
		outputMas.append(values.text)
	return outputMas

# Функция получения директории под музыку
def get_dirpath():
	path = '~/Downloads/vkmusic'
	if not os.path.exists(path):
		try:
			os.makedirs(path)
			return path
		except:
			print('Не удалось создать дерикторию ' + path)
			os.exit()
	return path

# Функция получения исполнителей, названий, ссылок
def get_music(doc):
	path = get_dirpath()
	tracks = list(zip(get_trackinfo('url', doc),
			get_trackinfo('title', doc),
			get_trackinfo('artist', doc)))
	for url, title, artist in tracks[:]:
		file_name = '{path}/{artist}-{title}.mp3'.format(
			path = path,
			artist = artist.replace(' ','\ '),
			title = title.replace(' ','\ ')
		)
		if os.path.exists(file_name):
			print('{file_name} уже загружен'.format(file_name = file_name))
		else:
			down_cmd = 'wget {url} -O {file_name}'.format(url = url, file_name = file_name)
			os.popen(down_cmd)
