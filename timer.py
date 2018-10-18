from threading import Timer
from pygame import mixer

def timeout():
    #mixer.init()
    mixer.music.stop()
    mixer.music.load('sound/beep.mp3')
    mixer.music.play()


def timer_set(timer):
    if timer > 0:
        print("Countdown to", str(timer), "seconds.")
        Timer(timer, timeout).start()


def translate_time(string):
    result_time = 0
    if string.find('时') != -1:
        hor_str = string[:string.find('时')]
        if hor_str[-1] == '小':
            hor_str = hor_str[:-1]
        string = string[string.find('时')+1:]
        #print("hor_str: ", hor_str)
        result_time += chinese_to_arabic(hor_str) * 3600
    
    if string.find('分') != -1:
        min_str = string[:string.find('分')]
        string = string[string.find('分')+1:]
        if string[0] == '钟':
            string = string[1:]
        #print("min_str: ", min_str)
        result_time += chinese_to_arabic(min_str) * 60

    if string.find('秒') != -1:
        sec_str = string[:string.find('秒')]
        #print("sec_str: ", sec_str)
        result_time += chinese_to_arabic(sec_str)

    return result_time

 
def chinese_to_arabic(cn_string):
    CN_NUM = {'〇' : 0, '一' : 1, '二' : 2, '三' : 3, '四' : 4, '五' : 5, '六' : 6, '七' : 7, '八' : 8, '九' : 9, '零' : 0, '两' : 2}
    CN_UNIT = {'十' : 10, '百' : 100, '千' : 1000, '万' : 10000, '亿' : 100000000}
    unit = 0   # current
    ldig = []  # digest

    for cndig in reversed(cn_string):
        if cndig in CN_UNIT:
            unit = CN_UNIT.get(cndig)
            if unit == 10000 or unit == 100000000:
                ldig.append(unit)
                unit = 1
        else:
            dig = CN_NUM.get(cndig)
            if unit:
                dig *= unit
                unit = 0
            ldig.append(dig)
    if unit == 10:
        ldig.append(10)
    val, tmp = 0, 0
    for x in reversed(ldig):
        if x == 10000 or x == 100000000:
            val += tmp * x
            tmp = 0
        else:
            tmp += x
    val += tmp
    return val


#timer_set(translate_time("十二秒钟"))
