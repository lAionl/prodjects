#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Модуль для работы с музыкой из vk.ru

import socket, os, lxml.html, re, urllib

# Функция для задания вопросов
def getquestion(question):
	answer = input(question + ' (Y/N)')
	if(answer.upper == 'Y'):
		return True
	elif(answer.upper == 'N'):
		return False
	else:
		print('Некорректный ввод попробуйте еще раз.')
		getquestion(question)

# Функция проверки соединения с сетью
def checkInet():
	try:
		socket.gethostbyaddr('www.yandex.ru')
	except socket.gaierror:
		return False
	return True

# Функция подключения к vk и получения списка музыки
def vkConnect(access_token, expires_in, user_id):
	url = "https://api.vkontakte.ru/method/audio.get.xml?uid=" + user_id + "&access_token=" + access_token
	page = urllib2.urlopen(url)
	html = page.read()
	doc = lxml.html.document_from(html)
	return doc

# Функция наполнения массива данными для getTrackInfo
def getTrackInfo(target_info, input_doc):
	outputMas = []
	for values in input_doc.cssselect(target_info):
		outputMas.append(target_info.text)
	return outputMas

# Функция получения директории под музыку
def getDirPath():
	path = 'vkmusic'
	if os.path.exists(path):
		return path
	else:
		os.makedirs(path)
		return path

# Функция получения исполнителей, названий, ссылок
def getMusic(doc):
	artistMas, titleMas, urlMas = []
	artistMas = getTrackInfo(artist, doc)
	titleMas = getTrackInfo(title, doc)
	urlMas = getTrackInfo(url, doc)
	path = getDirPath()
	for i in range(len(artistMas)):
		filename_new = path+"/"+artistMas[i]+" - "+titleMas[i]+".mp3"
		if os.path.exists(filename_new):
			print(filename_new + 'уже загружен')
		else:
			downCmd = "wget -P " + path + " " + urlMas[i]
			os.popen(downCmd)
			
			p = re.compile(r'[0-9a-zA-Z]+\.mp3$')
			filename = p.findall(urlMas[i])
			
			try:
				os.rename(path+'/'+filename[0],path+'/'+artistMas[i]+' - '+titleMas[i]+'.mp3')
			except:
				print('Невозможно переименовать.')
