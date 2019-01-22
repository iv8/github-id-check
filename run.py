#!/usr/bin/python
# coding:utf-8
import requests

char = '0123456789'
print('Begin Find\n------------------------------------')
for s1 in char:
    for s2 in char:
        if 404 == requests.head('https://github.com/' + s1 + s2).status_code:
            print(s1 + s2)
for s1 in char:
    for s2 in char:
        for s3 in char:
            if 404 == requests.head('https://github.com/' + s1 + s2 + s3).status_code:
            print(s1 + s2 + s3)
print('------------------------------------\nEnd Find')
