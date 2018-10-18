# -*- coding: utf-8 -*-
###  hardware_func.py  ###
###  功能：将串口传来的ADC数据存储到txt文件中  ###
import serial
import time
import RPi.GPIO as GPIO

class Hardware():

    def __init__(self, ser, channel1):
        self.ser = ser
        self.channel1 = channel1
        self.filename = "input_sound.txt"
        self.content = ""
        self.all_content = ""
        self.isreset = False
        self.time_start = 0
        self.time_end = 0
        self.overwrite = False
    
    
    def save_to_file(self):
        if self.overwrite == True:
            file_1 = open(self.filename, 'w+')
        else:
            file_1 = open(self.filename, 'a+')
        file_1.write(self.content)
        file_1.close()


    def reset_sound_data(self):
        if self.isreset == False:
            self.overwrite = True
            self.all_content = ""
            self.content = ""
            self.save_to_file()


    def hardware_setup(self):
        # 配置信号输入IO口
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(self.channel1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        # 打开串口
        if self.ser.isOpen() == False:
            print("Serial port on Pi is not open.")


    def wait_for_start_to_speak(self, mode):  # 读取声音串口数据
        print("Get ready to listen.")
        self.ser.flushInput()
        read_status = GPIO.input(self.channel1)
        while read_status == False:
            self.content = str(self.ser.read(20))[2:-1]
            #if self.content != '':
                #print(self.content, ' ')
            if self.content != '' and self.content[-1] == '0' and mode != 2:  #暂时离开状态
                return 2
            elif self.content != '' and self.content[-1] == '1' and mode == 2:  #暂时离开状态取消
                mode = 0
            elif self.content != '' and self.content[-1] == '2' and mode != 3:  #久坐提醒状态
                return 3
            elif self.content != '' and self.content[-1] == '1' and mode == 3:  #久坐提醒状态取消
                mode = 0
            time.sleep(0.005)
            read_status = GPIO.input(self.channel1)
            
        return mode


    def output_update(self, status):
        dat = '@' + str(status) + '#' + '0' + '#'
        self.ser.write(dat.encode('ascii'))


    def hardware_close(self):
        self.ser.close()
        #GPIO.cleanup()
