#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Модуль для работы с фото из vk.ru

Для модуля lxml установите пакет python3-lxml, а так же
выполните pip3 install cssselect
"""

import socket, os, urllib.error, urllib.parse, requests
from json import load


def check_inet():
    try:
        socket.gethostbyaddr('www.yandex.ru')
    except socket.gaierror:
        return False
    return True

def post_photo_to_vk(access_token, user_id, aid,input_dir):
    url = 'https://api.vk.com/method/photos.getUploadServer?aid='+ aid +'&uid=' + user_id + '&access_token=' + access_token
    resp = requests.post(url).json()
    try:
        upload_url = resp['response']['upload_url']
    except:
        return -1
    files_array = (os.listdir(path=input_dir))
    for files in files_array:
        path = (input_dir+'/'+files)
        datagen = {'file1':open(path,'rb')}
        conn = requests.post(upload_url, files=datagen).json()
        fin_url = 'https://api.vk.com/method/photos.save?server='+str(conn['server'])+'&photos_list='+conn['photos_list']+'&album_id='+str(conn['aid'])+'&hash='+conn['hash']+'&uid=' + user_id + '&access_token=' + access_token
        upload_pict = requests.post(fin_url)

def get_photo_from_vk(user_id, aid):
    url = 'https://api.vk.com/method/photos.get?aid='+ aid +'&uid=' + user_id
    resp = requests.post(url).json()



def get_dir_to_download_path(path):
    if not os.path.exists(path):
        print('Не удалось найти директорию' + path)
        os.exit()
    return path

def get_credentials(credential_file_name = 'credentials.json'):
    with open(credential_file_name) as credential_file:
        credentials_dict = load(credential_file)
    token = credentials_dict.get('token')
    user_id = credentials_dict.get('user_id')
    aid = credentials_dict.get('aid')
    return token, user_id, aid


def main():
    pass

if __name__ == "__main__":
    exit(main())