#-*- coding: utf-8 -*-
###  ai_func.py  ###
###  功能：将wav声音文件借助百度AI的SDK识别成文字  ###
import requests
from aip import AipSpeech
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from urllib import parse
from urllib import request
import json
import weather_func
from city import city_dict
import bjtime
import baike
import tomato_clock
import timetable
import VOA
import timer
import memo

class Ai():
    def __init__(self):
        self.APP_ID = '??????'  #省去API信息
        self.API_KEY = '??????'  #省去API信息
        self.SECRET_KEY = '??????'  #省去API信息
        self.filePath = "input_sound.wav"
        self.result = []
        self.success = False
        self.pit = 2
        self.speed = 4
        self.set_response = {'你好，': '摁，你好，我是小祥，是你的智能学习伴侣哦！',
                             '开灯，': '摁，好的，马上帮你开灯！',
                             '开的，': '摁，好的，马上帮你开灯！',
                             '关灯，': '摁，真的舍得跟我说再见吗？那，下次再见。',
                             '关的，': '摁，真的舍得跟我说再见吗？那，下次再见。',
                             '喂，': '摁，来啦。我就是人见人爱，花见花开的小祥。',
                             '为，': '摁，来啦。我就是人见人爱，花见花开的小祥。',
                             '秀一波，': '摁，什么？叫我秀一波？看不起我吗？这就秀给你看！',
                             '肖一波，': '摁，什么？叫我秀一波？看不起我吗？这就秀给你看！',
                             '秀波，': '摁，什么？叫我秀一波？看不起我吗？这就秀给你看！',
                             '秀一，': '摁，什么？叫我秀一波？看不起我吗？这就秀给你看！',
                             '修一，': '摁，什么？叫我秀一波？看不起我吗？这就秀给你看！',
                             'q1，': '摁，什么？叫我秀一波？看不起我吗？这就秀给你看！',
                             '放首歌，': '摁，小伙子还挺有情调的，来，这就给你放。',
                             '来首歌，': '摁，小伙子还挺有情调的，来，这就给你放。',
                             '上一首，': '摁，听不够？DJ，再来。',
                             '下一首，': '摁，好的。DJ，切歌！',
                             '调大声，': '摁，好的。DJ，加大马力！',
                             '调小声，': '摁，吵到隔壁老王了吧，DJ，小声一点。',
                             '关音乐，': '摁，吵到隔壁老王了吗？马上帮你关了。',
                             '观音说，': '摁，吵到隔壁老王了吗？马上帮你关了。',
                             '老子吃火锅，': '摁，老子坐火车，你坐火车轨道；老子上北大，你上北大青鸟；老子娶天仙，你娶天线宝宝；老子吹空调，你吹空调外机；老子吃西瓜，你吃西瓜皮皮；老子吃泡面，你吃调味料包；老子吃凤爪，你吃陈年泡椒；老子喝酸奶，你舔酸奶盖盖，老子吃辣条，你舔塑料袋袋。',
                             '我吃火锅，': '摁，老子坐火车，你坐火车轨道；老子上北大，你上北大青鸟；老子娶天仙，你娶天线宝宝；老子吹空调，你吹空调外机；老子吃西瓜，你吃西瓜皮皮；老子吃泡面，你吃调味料包；老子吃凤爪，你吃陈年泡椒；老子喝酸奶，你舔酸奶盖盖，老子吃辣条，你舔塑料袋袋。',
                             '我帅吗？': '摁，帅，但你仍要好好学习不能骄傲，要不然别人会说你除了帅一无是处，别人都是有故事的，而你活到现在却只有这个帅字贯穿一生，你一直默默承受着这个年纪不应有的帅气，唉，真是太累了。',
                             '我帅吧，': '摁，帅，但你仍要好好学习不能骄傲，要不然别人会说你除了帅一无是处，别人都是有故事的，而你活到现在却只有这个帅字贯穿一生，你一直默默承受着这个年纪不应有的帅气，唉，真是太累了。',
                             '几点，': '',
                             '几点了，': '',
                             '时间，': '',
                             '打开番茄，': '摁，好的，番茄钟已打开。',
                             '打开番茄钟，': '摁，好的，番茄钟已打开。',
                             '关闭番茄，': '摁，好的，番茄钟已关闭。',
                             '关闭番茄钟，': '摁，好的，番茄钟已关闭。',
                             }
    
    
    def get_file_content(self):
        with open(self.filePath, 'rb') as fp:
            return fp.read()


    def set_file_content(self):
        if not isinstance(self.result, dict):
            with open(self.filePath, 'wb') as f:
                f.write(self.result)


    def ai_process(self, channel2_status, music_status, mode, c_city):
        print("Recognizing sound...")
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

        client = AipSpeech(self.APP_ID, self.API_KEY, self.SECRET_KEY)

        self.filePath = 'input_sound.wav'
        self.result = client.asr(self.get_file_content(), 'wav', 16000, {'dev_pid': '1536'})


        if self.result.get('err_no') == 3301:
            print("Speech quality error, please try again.")
            response_text = "主人，说话大声一点呀，我没听清。"
                
        else:
            self.success = True
            #print(self.result)
            dict1_value = self.result.get('result')[0]
            print("Text: ", dict1_value)

            # You can add text here to debug communication
            #dict1_value = "十一秒倒计时，"
            
            if self.set_response.get(dict1_value) != None:
                response_text = self.set_response.get(dict1_value)
            else:
                response_text = dict1_value
            
            # < 聊天模式 mode = 1 >
            if dict1_value.find("聊天") != -1 or dict1_value.find("图灵") != -1:
                if dict1_value.find("不") != -1 or dict1_value.find("关") != -1:
                    mode = 0
                    response_text = '摁，聊天模式关闭，图灵机器人走了。'
                else:
                    mode = 1
                    response_text = '摁，聊天模式开启，图灵机器人，快过来聊天吧！'
            
            #获取聊天内容
            elif mode == 1:
                self.pit = 4
                response_text = '摁，' + self.turingChat(dict1_value)
            
            
            # < 正常模式 mode = 0 >
            else:
                #离开模式，准备待机
                if dict1_value.find("走了") != -1 or dict1_value.find("拜拜") != -1 or dict1_value.find("再见") != -1 or dict1_value.find("上学") != -1:
                    self.speed = 5
                    channel2_status = 0
                    music_status = 0
                    wea_str = weather_func.get_weather_lite(c_city, city_dict[c_city])
                    day_str_temp = bjtime.get_Beijing_day()
                    [day0, time0] = timetable.translate_time(day_str_temp[0], day_str_temp[1])
                    day_str = timetable.read_timetable(day0, time0)
                    
                    response_text = "摁，进入离开模式，灯和音乐已关闭，" + day_str + wea_str + "一路顺风。"

                #备忘录读取
                elif dict1_value == "备忘，":
                    temp_str1 = memo.memo_read()
                    if temp_str1 != "":
                        response_text = "摁，备忘录内容如下。" + temp_str1
                    else:
                        response_text = "摁，备忘录是空的哦。"
                #备忘录清空
                elif dict1_value.find("备忘") != -1 and dict1_value.find("清空") != -1:
                    memo.memo_clean()
                    response_text = "摁，备忘录已经帮你清空。"
                #备忘录读取
                elif dict1_value.find("备忘") != -1:
                    temp_str1 = dict1_value.replace("备忘", "")
                    memo.memo_write(temp_str1)
                    response_text = "摁，已经帮你记录备忘，" + temp_str1
                
                #调整语速
                elif dict1_value == '老子吃火锅，' or dict1_value == '我吃火锅，' or dict1_value == '我帅吗？' or dict1_value == '我帅吧，':
                    self.speed = 6
                    
                #查询北京时间
                elif dict1_value == "几点，" or dict1_value == "几点了，" or dict1_value == "时间，":
                    response_text = '摁，' + bjtime.get_Beijing_time()
                
                #搜索百度百科
                elif dict1_value[-4:] == '是什么？' or dict1_value[-4:] == '是什么，':
                    response_text = '摁，' + baike.baike_search(dict1_value[:-4])
                    self.speed = 6
                elif dict1_value[-3:] == '是谁？' or dict1_value[-3:] == '是谁，':
                    response_text = '摁，' + baike.baike_search(dict1_value[:-3])
                    self.speed = 6
                
                #中文翻译成英文
                elif dict1_value.find("翻译") != -1:
                    temp_str1 = dict1_value.replace("翻译", "")
                    temp_str2 = baike.translate_C2E(temp_str1)
                    response_text = '摁，' + temp_str1 + '的翻译结果是，' + temp_str2
                
                #听英语听力VOA
                elif dict1_value.find("英语") != -1 or dict1_value.find("VOA") != -1:
                    if dict1_value.find("慢") != -1:
                        response_text = '摁，' + VOA.VOA_search(False)
                    else:
                        response_text = '摁，' + VOA.VOA_search(True)
                
                #番茄钟操作
                elif dict1_value == "打开番茄，" or dict1_value == "打开番茄钟，":
                    tomato_clock.start()
                elif dict1_value == "关闭番茄，" or dict1_value == "关闭番茄钟，":
                    tomato_clock.end()
                
                #倒计时操作
                elif dict1_value.find("倒计时") != -1 or dict1_value.find("计时") != -1 or dict1_value.find("定时") != -1:
                    dict1_value = dict1_value.replace("倒计时", "")
                    dict1_value = dict1_value.replace("计时", "")
                    dict1_value = dict1_value.replace("定时", "")
                    dict1_value = dict1_value.replace("，", "")
                    timer.timer_set(timer.translate_time(dict1_value))
                    response_text = '摁，为你设定定时' + dict1_value + '。'
                
                #获取课程表
                elif dict1_value.find("课表") != -1:
                    self.speed = 5
                    if dict1_value.find("周") != -1:
                        temp_str1 = dict1_value[dict1_value.find("周")+1]
                    elif dict1_value.find("星期") != -1:
                        temp_str1 = dict1_value[dict1_value.find("星期")+2]
                    else:
                        temp_str1 = ""
                    if dict1_value.find("上午") != -1 or dict1_value.find("早上") != -1:
                        temp_str2 = "上午"
                    elif dict1_value.find("下午") != -1:
                        temp_str2 = "下午"
                    elif dict1_value.find("晚上") != -1:
                        temp_str2 = "晚上"
                    else:
                        temp_str2 = "全天"
                    
                    if temp_str1 != "":
                        [day0, time0] = timetable.translate_time(temp_str1, temp_str2)
                        response_text = '摁，' + timetable.read_timetable(day0, time0)
                    else:
                        response_text = '摁，你要查哪一天的课表呢？'
                
                #设置当前城市
                elif dict1_value[0:2] == "我在":
                    dict1_value = dict1_value[2:-1]
                    if city_dict[dict1_value]:  #能找到城市
                        response_text = '摁，已将当前城市设置为' + dict1_value
                        c_city = dict1_value
                    else:
                        response_text = '摁，对不起，找不到你说的城市。'
                
                #查询城市天气
                try:
                    city_code = city_dict[dict1_value[:-1]]
                except:
                    city_code = ""
                if city_code:
                    response_text = '摁，' + weather_func.get_weather(dict1_value[:-1], city_code)
        
        
        #串口发送信息处理
        # < 离开模式 mode = 2 >
        if mode == 2:
            channel2_status = 0
            music_status = 0
            dict1_value = ''
            response_text = "摁，主人不在身旁，自动进入离开模式，灯和音乐已关闭。"
            
        # < 久坐提醒模式 mode = 3 >
        elif mode == 3:
            mode = 0
            dict1_value = ''
            response_text = "摁，你已经坐太久了，起来运动一下吧！"
        
        print("Response: ", response_text)
        response = client.synthesis(response_text, 'zh', 1, {'vol': 6, 'pit': self.pit, 'spd': self.speed})
        self.filePath = 'response.mp3'
        self.result = response
        self.set_file_content()
        
        
        if self.success == True:
            if response_text == '摁，真的舍得跟我说再见吗？那，下次再见。':
                return [0, 0, mode, c_city]
            elif response_text == '摁，好的，马上帮你开灯！':
                return [1, music_status, mode, c_city]
            elif response_text == '摁，什么？叫我秀一波？看不起我吗？这就秀给你看！':
                return [2, music_status, mode, c_city]
            elif response_text == '摁，小伙子还挺有情调的，来，这就给你放。':
                return [channel2_status, 1, mode, c_city]
            elif response_text == '摁，听不够？DJ，再来。':
                return [channel2_status, 2, mode, c_city]
            elif response_text == '摁，好的。DJ，切歌！':
                return [channel2_status, 3, mode, c_city]
            elif response_text == '摁，好的。DJ，加大马力！':
                return [channel2_status, 4, mode, c_city]
            elif response_text == '摁，吵到隔壁老王了吧，DJ，小声一点。':
                return [channel2_status, 5, mode, c_city]
            elif response_text == '摁，吵到隔壁老王了吗？马上帮你关了。':
                return [channel2_status, 0, mode, c_city]
            else:
                return [channel2_status, music_status, mode, c_city]
        else:
            return [channel2_status, music_status, mode, c_city]


    def turingChat(self, question):
        KEY = '8afba6fdc75544f0bebc465615da1e0b'  # change to your API KEY
        url = 'http://www.tuling123.com/openapi/api'
        req_info = question.encode('utf-8')

        query = {'key': KEY, 'info': req_info}
        headers = {'Content-type': 'text/html', 'charset': 'utf-8'}

        try:
            #用requests模块get方式获取内容
            r = requests.get(url, params=query, headers=headers)
            res = r.text
            result = json.loads(res).get('text').replace('<br>', '\n')
        except:
            result = "抱歉，我听不懂。"

        return result

