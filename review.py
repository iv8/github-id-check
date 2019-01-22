#!/usr/bin/python
# coding:utf-8

import requests
import requests

latest = requests.get('https://raw.githubusercontent.com/l26/get-id/master/id.list').text
latest = latest[0:len(latest) - 1]
idList = latest.split('\n')

# 获得一个新的 API authenticity_token
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
    
# 获取对应 username status_code
def getCode(form):
    try:
        code = http.post('https://github.com/signup_check/username', data=form).status_code
        if code == 429: # GitHub API 请求频繁被封禁 IP
            time.sleep(5)
            res = getRes()
            return getCode(form)
        return code
    except Exception as e:
        getCode(form)

res = getRes()

for id in idList:
    form = {"referer": "https://github.com", 'authenticity_token': res, 'value': id}
    code = getCode(form)
    print(str(code) + ': '+ id)
