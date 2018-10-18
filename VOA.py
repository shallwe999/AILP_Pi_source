#-*- coding:utf-8 -*-
from urllib.parse import quote
from urllib.request import urlopen
from bs4 import BeautifulSoup
from threading import Timer
import re
import requests
from pygame import mixer

def VOA_search(standard=True):
    try:
        if standard == True:
            url_str = 'VOA_Standard_English/'
            idx_num = 0
            response_str = ' VOA standard '
        else:
            url_str = 'VOA_Special_English/'
            idx_num = 1
            response_str = ' VOA special '

        resp1 = urlopen('http://www.51voa.com/' + url_str)
        soup1 = BeautifulSoup(resp1, 'html.parser')
        scope1 = soup1.select('a[target="_blank"]')  #查找类为a且target为_blank的标签
        latest_url = scope1[idx_num].attrs['href']

        resp2 = urlopen('http://www.51voa.com' + latest_url)
        soup2 = BeautifulSoup(resp2, 'html.parser')
        scope2 = soup2.select('a[id="mp3"]')  #查找id为mp3的标签
        mp3_url = scope2[0].attrs['href']
        
        Timer(3.5, VOA_download, (mp3_url,)).start()  #开启另一个线程下载文件

        return "马上为你播放最新" + response_str + "，正在下载。"
    except:
        return "对不起，找不到" + response_str + "，请检查连接。"


def VOA_download(mp3_url):
    print("Downloading VOA MP3.")
    r = requests.get(mp3_url) 
    with open("sound/VOA.mp3", "wb") as code:
        code.write(r.content)
    print("VOA MP3 downloaded, ready to play.")

    #mixer.init()
    mixer.music.load('sound/VOA.mp3')
    mixer.music.play()

