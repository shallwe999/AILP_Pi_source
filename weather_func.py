from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

def get_weather(city, city_code):

    resp = urlopen('http://www.weather.com.cn/weather/' + city_code + '.shtml')   
    soup = BeautifulSoup(resp,'html.parser')
    tagToday = soup.find('p',class_="tem")  #第一个包含class="tem"的p标签即为存放今天天气数据的标签

    try:
        temperature_1_High = tagToday.span.string  #有时候这个最高温度是不显示的
    except AttributeError as e:
        temperature_1_High = ""

    temperature_1_Low = tagToday.i.string  #获取今天最低温度
    temperature_2_High = tagToday.find_next('p',class_="tem").span.string  #获取明天最高温度
    temperature_2_Low = tagToday.find_next('p',class_="tem").i.string  #获取明天最低温度

    weather_1 = soup.find('p',class_="wea").string  #获取今天天气
    weather_2 = tagToday.find_next('p',class_="wea").string

    if temperature_1_High == "":
        return city + "，今晚" + weather_1 + "，最低" + temperature_1_Low[:-1] + "度，明天" + weather_2 + "，" + temperature_2_Low[:-1] + "至" + temperature_2_High[:-1] + "度。"
    else:
        return city + "，今天" + weather_1 + "，"  + temperature_1_Low[:-1] + "度，明天" + weather_2 + "，" + temperature_2_Low[:-1] + "至" + temperature_2_High + "度。"



def get_weather_lite(city, city_code):

    resp = urlopen('http://www.weather.com.cn/weather/' + city_code + '.shtml')   
    soup = BeautifulSoup(resp,'html.parser')
    tagToday = soup.find('p',class_="tem")  #第一个包含class="tem"的p标签即为存放今天天气数据的标签

    try:
        temperature_1_High = tagToday.span.string  #有时候这个最高温度是不显示的
    except AttributeError as e:
        temperature_1_High = ""

    temperature_1_Low = tagToday.i.string  #获取今天最低温度
    weather_1 = soup.find('p',class_="wea").string  #获取今天天气

    if temperature_1_High == "":
        return city + "今晚" + weather_1 + "，最低" + temperature_1_Low[:-1] + "度。"
    else:
        return city + "今天" + weather_1 + "，"  + temperature_1_Low[:-1] + "度。"


