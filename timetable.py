#-*- coding:utf-8 -*-
from urllib.request import urlretrieve

def download_timetable():
    urlretrieve('https://raw.githubusercontent.com/shallwe999/AILP_info/master/timetable.csv', './timetable.csv')


def read_timetable(day, time=0):
    table_data = []
    table_sound = ""
    found_table = False
    start_end_list = [1, 4, 5, 8, 9, 11]  #上午课时数，下午课时数，晚上课时数

    with open("timetable.csv","r" ,encoding = "utf-8-sig") as f:
        for line in f:
            table_data.append( (line.strip() + ',').split(',') )  #加逗号防止寻索引溢出

    idx = 1
    table_sound = table_data[day][0]

    if time == 0:  #全天课表
        while table_data[day][idx] != '':
            found_table = True
            table_sound = table_sound + "第" + str(table_data[day][idx]) + "至" + str(table_data[day][idx+1]) + "节的课为"
            table_sound = table_sound + table_data[day][idx+2] + "，地点在" + table_data[day][idx+3] + "，"
            idx = idx + 4

    elif time == 1:  #上午课表
        table_sound = table_sound + "上午"
        while table_data[day][idx] != '':
            if int(table_data[day][idx]) >= start_end_list[0] and int(table_data[day][idx]) <= start_end_list[1]:
                found_table = True
                table_sound = table_sound + "第" + str(table_data[day][idx]) + "至" + str(table_data[day][idx+1]) + "节的课为"
                table_sound = table_sound + table_data[day][idx+2] + "，地点在" + table_data[day][idx+3] + "，"
            idx = idx + 4

    elif time == 2:  #下午课表
        table_sound = table_sound + "下午"
        while table_data[day][idx] != '':
            if int(table_data[day][idx]) >= start_end_list[2] and int(table_data[day][idx]) <= start_end_list[3]:
                found_table = True
                table_sound = table_sound + "第" + str(table_data[day][idx]) + "至" + str(table_data[day][idx+1]) + "节的课为"
                table_sound = table_sound + table_data[day][idx+2] + "，地点在" + table_data[day][idx+3] + "，"
            idx = idx + 4

    elif time == 3:  #晚上课表
        table_sound = table_sound + "晚上"
        while table_data[day][idx] != '':
            if int(table_data[day][idx]) >= start_end_list[4] and int(table_data[day][idx]) <= start_end_list[5]:
                found_table = True
                table_sound = table_sound + "第" + str(table_data[day][idx]) + "至" + str(table_data[day][idx+1]) + "节的课为"
                table_sound = table_sound + table_data[day][idx+2] + "，地点在" + table_data[day][idx+3] + "，"
            idx = idx + 4

    if found_table == False:
        table_sound = table_sound + "没有课哦！"

    return table_sound


def translate_time(str1, str2):
    day = 0
    if str1[-1] == "一":
        day = 0
    elif str1[-1] == "二":
        day = 1
    elif str1[-1] == "三":
        day = 2
    elif str1[-1] == "四":
        day = 3
    elif str1[-1] == "五":
        day = 4
    elif str1[-1] == "六":
        day = 5
    elif str1[-1] == "日" or str1[-1] == "天":
        day = 6

    time = 0
    if str2 == "全天" or str2 == "整天" or str2 == "一整天":
        time = 0
    elif str2 == "上午" or str2 == "早上":
        time = 1
    elif str2 == "下午":
        time = 2
    elif str2 == "晚上":
        time = 3

    return [day, time]
