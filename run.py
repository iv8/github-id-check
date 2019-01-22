#!/usr/bin/python
# coding:utf-8
import requests
import re
import time
char = 'z4e,z4h,z4j,z4o,z4s,z4u,z4v,z4w,z4y,z50,z51,z54,z5a,z5b,z5c,z5d,z5f,z5g,z5i,z5j,z5k,z5l,z5n,z5o,z5p,z5q,z5t,z5u,z5v,z5w,z5x,z5y,z5-,z60,z65,z67,z68,z69,z6a,z6b,z6c,z6d,z6e,z6f,z6g,z6h,z6i,z6j,z6k,z6l,z6m,z6n,z6o,z6q,z6r,z6s,z6t,z6u,z6w,z6y,z6z,z6-,z75,z7a,z7b,z7c,z7d,z7e,z7f,z7h,z7i,z7j,z7l,z7m,z7n,z7o,z7p,z7q,z7r,z7s,z7t,z7u,z7v,z7w,z7-,z82,z84,z85,z88,z89,z8a,z8b,z8c,z8f,z8g,z8h,z8i,z8j,z8m,z8p,z8q,z8s,z8t,z8u,z8v,z8w,z8x,z8y,z8-,z98,z9a,z9b,z9c,z9d,z9e,z9f,z9i,z9j,z9k,z9l,z9o,z9p,z9q,z9r,z9t,z9u,z9v,z9y,z9-,za5,za6,za7,zb4,zb5,zb6,zb7,zb9,zb-,zc4,zc6,zc-,zd2,zd4,zd5,zd6,zd7,zd8,zdq,zd-,ze3,ze6,ze7,ze8,ze9,zf3,zf6,zf7,zf8,zf9,zfv,zf-,zg4,zg7,zg8,zg9,zg-,zh5,zh6,zh8,zi5,zi-,zj2,zj5,zj6,zj7,zj-,zk3,zk5,zk6,zk8,zl4,zl5,zl7,zl8,zm6,zm9,zm-,zn1,zn5,zn6,zn8,zn9,zo4,zo5,zo8,zo-'
char = char.split(',')
print('Begin Find\n------------------------------------')
http = requests.Session()
def getRes():
    res = http.get("https://github.com").text
    loc1 = re.search('auto-check src="\/signup_check\/username" csrf="(\S+)"', res).span()
    res = res[loc1[0]:loc1[1]]
    loc2 = re.search('csrf="', res).span()
    res = res[loc2[1]:len(res) - 1]
    return res
def getCode(form):
    code = http.post('https://github.com/signup_check/username', data=form).status_code
    if code == 429:
        time.sleep(5)
        res = getRes()
        return getCode(form)
    return code
res = getRes()
for value in char:
    form = {"referer":"https://github.com",'authenticity_token':res,'value':value}
    code = getCode(form)
    print(str(code) + ': '+ value)
print('------------------------------------\nEnd Find')
