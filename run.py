#!/usr/bin/python
# coding:utf-8
import requests
import re
import time
char = '06,045,048,049,060,061,062,064,065,067,082,083,087,094,115,116,134,144,158,185,191,211,214,232,258,278,279,283,302,319,362,363,367,374,378,379,387,395,397,400,401,402,403,405,406,407,408,409,411,412,413,414,415,416,417,418,419,421,423,424,425,426,427,428,430,431,433,436,442,455,469,472,473,476,484,485,489,495,501,504,505,506,507,508,509,510,511,557,558,565,566,994'
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
    print(str(code) + value)
print('------------------------------------\nEnd Find')
