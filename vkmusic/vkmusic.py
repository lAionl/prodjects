#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Модуль для работы с музыкой из vk.ru

Для модуля lxml установите пакет python3-lxml, а так же
выполните pip3 install cssselect
"""
import socket, os, lxml.html, urllib.request, urllib.error
from json import load


def check_inet():
    """Функция проверки соединения с сетью."""
    try:
        socket.gethostbyaddr('www.yandex.ru')
    except socket.gaierror:
        return False
    return True


def vk_connect(access_token, user_id):
    """Функция подключения к vk и получения списка музыки."""
    url = "https://api.vkontakte.ru/method/audio.get.xml?uid=" + user_id + "&access_token=" + access_token
    try:
        page = urllib.request.urlopen(url)
    except urllib.error.URLError as e:
        print(e + '\nПроверьте правильность token для ' + user_id + ',\nтекущее значение = ' + access_token)
        os.exit()
    html = page.read()
    doc = lxml.html.document_fromstring(html)
    return doc


def get_trackinfo(target_info, input_doc):
    """Функция наполнения массива данными для getTrackInfo."""
    output_arr = []
    for values in input_doc.cssselect(target_info):
        output_arr.append(values.text)
    return output_arr


def get_dir_to_download_path(path):
    """Функция получения директории для загрузки музыки."""
    if not os.path.exists(path):
        try:
            os.makedirs(path)
            return path
        except:
            print('Не удалось создать дерикторию ' + path)
            os.exit()
    return path

def get_credentials(credential_file_name = 'credentials.json'):
    """
    Функция для получения access_token и user_id из файла переданного как аргумент
    формат содержимого файла:
    {
        "token":"<ваш_token>"
        "user_id":"<ваш_user_id>"
    }
    """
    with open(credential_file_name) as credential_file:
        credentials_dict = load(credential_file)
    token = credentials_dict.get('token')
    user_id = credentials_dict.get('user_id')
    return token, user_id

def get_music(doc, dir_to_download_path = '/tmp/vkmusic'):
    """Функция получения исполнителей, названий, ссылок."""
    dir_to_download_path = get_dir_to_download_path(dir_to_download_path)
    tracks = list(zip(get_trackinfo('url', doc),
                      get_trackinfo('title', doc),
                      get_trackinfo('artist', doc)))
    for url, title, artist in tracks[:]:
        file_name = '{path}/{artist}-{title}.mp3'.format(
            path=dir_to_download_path,
            artist=artist,
            title=title
        )
        if os.path.exists(file_name):
            print('{file_name} уже загружен'.format(file_name=file_name))
        else:
            try:
                urllib.request.urlretrieve(url, file_name)
            except:
                print('OMFG! {file_name} is missing!!!'.format(file_name=file_name))
