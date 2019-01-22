#!/usr/bin/python
# coding:utf-8

import requests

latest = requests.get('https://raw.githubusercontent.com/l26/get-id/master/id.list').text
latest = latest[0:len(latest) - 1]
idList = latest.split('\n')
char = 'abcdefghijklmnopqrstuvwxyz'
num = '0123456789'
for id in idList:
    # e.g.
    # 查找一个全英文的 GitHub ID 
    if char.find(id[0]) != -1 and char.find(id[1]) != -1 and char.find(id[2]) != -1:
        print(id)
