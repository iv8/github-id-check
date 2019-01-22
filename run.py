#!/usr/bin/python
# coding:utf-8
import requests
import re
import time

char = '0123456789abcdefghijklmnopqrstuvwxyz-'

print('Begin Find\n------------------------------------')
http = requests.Session()

def getRes():
    try:
        res = http.get("https://github.com").text
        loc1 = re.search('auto-check src="\/signup_check\/username" csrf="(\S+)"', res).span()
        res = res[loc1[0]:loc1[1]]
        loc2 = re.search('csrf="', res).span()
        res = res[loc2[1]:len(res) - 1]
        return res
    except Exception as e:
        return getRes()
    
def getCode(form):
    try:
        code = http.post('https://github.com/signup_check/username', data=form).status_code
        if code == 429:
            time.sleep(5)
            res = getRes()
            return getCode(form)
        return code
    except Exception as e:
        getCode(form)

res = getRes()

# code: 422 不可用, 200 可注册
for s1 in char:
    form = {"referer": "https://github.com", 'authenticity_token': res, 'value': s1}
    code = getCode(form)
    print(str(code) + ': '+ s1)
    for s2 in char:
        form = {"referer": "https://github.com", 'authenticity_token': res, 'value': s1 + s2}
        code = getCode(form)
        print(str(code) + ': '+ s1 + s2)
        for s3 in char:
            form = {"referer": "https://github.com", 'authenticity_token': res, 'value': s1 + s2 + s3}
            code = getCode(form)
            print(str(code) + ': '+ s1 + s2 + s3)

print('------------------------------------\nEnd Find')
