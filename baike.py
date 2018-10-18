#-*- coding:utf-8 -*-
from urllib.parse import quote
from urllib.request import urlopen
from bs4 import BeautifulSoup
from requests import post
import re
import json

def baike_search(search_word, multi_code=""):
    try:
        search_word_url = quote(search_word, encoding='utf-8')
        resp = urlopen('https://baike.baidu.com/item/' + search_word_url + multi_code)
        soup = BeautifulSoup(resp, 'html.parser')
        desc = soup.find('meta', attrs={"name":"description"})
        temp = str(desc)
        desc = temp[temp.find('content="')+9 : temp.find('。')+1]
        if desc == "":  #出现多义词的情况
            soup_next = soup.find(text='多义词')
            mul_pos = soup_next.find_next('div').a.attrs['data-lemmaid']  #获取多义词首个的网址
            desc = baike_search(search_word, multi_code='/'+mul_pos)
        return desc
    except:
        return "对不起，我没法在百度百科搜到哦，换个词试试。"

def translate_C2E(trans_str):
    url = "http://fanyi.baidu.com/basetrans"
    data = {'from':'zh', 'to':'en', 'query': trans_str,}
    headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36",}
    response = post(url, data=data, headers=headers)
    result = response.json()['trans'][0]['dst']
    return result
