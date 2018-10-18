import http.client

def get_Beijing_time():
    try:
        conn = http.client.HTTPConnection("www.beijing-time.org")
        conn.request("GET", "/time.asp")
        response = conn.getresponse()
        #print(response.status, response.reason)
        if response.status == 200:
            result = response.msg._headers[5][1]    
            data = result[-12:-4]  #获得了GMT时间
            hrs = int(data[0:2]) + 8
            if hrs >= 24:
                hrs = hrs - 24
            minute = int(data[3:5])
            sec = int(data[6:8])
            beijingTime = "北京时间，%s时%s分%s秒。" % (hrs, minute, sec)
        return beijingTime
    except:
        return "连接时间服务器出现问题，请检查后重试。"


def get_Beijing_day():
    day_list = ['一', '二', '三', '四', '五', '六', '日']
    try:
        conn = http.client.HTTPConnection("www.beijing-time.org")
        conn.request("GET", "/time.asp")
        response = conn.getresponse()
        #print(response.status, response.reason)
        if response.status == 200:
            result = response.msg._headers[5][1]     
            data = result[-12:-4]  #获得了GMT时间
            day_str = result[0:3]  #获得星期几

            if day_str == "Mon":
                day = 1
            elif day_str == "Tue":
                day = 2
            elif day_str == "Wed":
                day = 3
            elif day_str == "Thu":
                day = 4
            elif day_str == "Fri":
                day = 5
            elif day_str == "Sat":
                day = 6
            elif day_str == "Sun":
                day = 7

            hrs = int(data[0:2]) + 8
            if hrs >= 24:
                hrs = hrs - 24
                day = day + 1
                if day == 8:
                    day = 1
            day_result = "星期" + day_list[day-1]
            
            if hrs >= 4 and hrs <= 11:
                stage = '上午'
            elif hrs >= 12 and hrs <= 17:
                stage = '下午'
            else:
                stage = '晚上'
        return [day_result, stage]
    except:
        return "连接时间服务器出现问题，请检查后重试。"


#print(get_Beijing_time())
#print(get_Beijing_day())
