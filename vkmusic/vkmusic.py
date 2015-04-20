#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""Модуль для работы с музыкой из vk.ru"""

# Для модуля lxml установите пакет python-lxml, а так же
# выполните pip install cssselect
import socket, os, lxml.html, re, urllib.request

# Функция проверки соединения с сетью
def checkInet():
	try:
		socket.gethostbyaddr('www.yandex.ru')
	except socket.gaierror:
		return False
	return True

# Функция подключения к vk и получения списка музыки
def vkConnect(access_token, user_id):
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
def getTrackInfo(target_info, input_doc):
	outputMas = []
	for values in input_doc.cssselect(target_info):
		outputMas.append(values.text)
	return outputMas

# Функция получения директории под музыку
def getDirPath():
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
def getMusic(doc):
	artistMas = []
	titleMas = []
	urlMas = []
	artistMas = getTrackInfo('artist', doc)
	titleMas = getTrackInfo('title', doc)
	urlMas = getTrackInfo('url', doc)
	path = getDirPath()
	for i in range(len(artistMas)):
		filename_new = path + "/" + artistMas[i].replace(' ','\ ') + "-" + titleMas[i].replace(' ','\ ') + ".mp3"
		if os.path.exists(filename_new):
			print(filename_new + 'уже загружен')
		else:
			downCmd = "wget " + urlMas[i] + " -O " + filename_new
			os.popen(downCmd)
