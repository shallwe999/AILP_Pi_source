# -*- coding: utf-8 -*-
from hardware_func import Hardware
from wav_func import Wav
from ai_func import Ai
from pygame import mixer
from timetable import download_timetable
import RPi.GPIO as GPIO
import music_func
import serial
import time

def main():
    ser = serial.Serial("/dev/ttyAMA0", 115200, bytesize=8, parity='N', stopbits=1, timeout=0.2)
    channel1 = 40  #GPIO.29
    speaking_data = ""
    hardware_1 = Hardware(ser, channel1)
    download_timetable()

    music_lists = ['Attention - Charlie Puth.mp3', 'Counting Stars - OneRepublic.mp3',
                   'See You Again - Wiz Khalifa,Charlie Puth.mp3', 'Sugar - Maroon 5.mp3',
                   'Lost Stars - Adam Levine.mp3', 'Get Lucky - Daft Punk (feat. Pharrell Williams).mp3']
    
    channel2_status = 0
    music_status = 0
    playing_number = 0
    mode = 0
    c_city = '东莞'
    
    time.sleep(0.1)
    mixer.init()
    mixer.music.load('sound/welcome.mp3')
    mixer.music.play()
    
    hardware_1.hardware_setup()
    hardware_1.output_update(channel2_status)
    wav_1 = Wav()
    
    print('Welcome to AI learning partner!')
    
    while True:
        mode = hardware_1.wait_for_start_to_speak(mode)

        if mode != 2 and mode != 3:
            wav_1.record_to_wav()

        ai_1 = Ai()
        [channel2_status, music_status, mode, c_city] = ai_1.ai_process(channel2_status, music_status, mode, c_city)

        if mixer.music.get_busy() == True:
            mixer.music.fadeout(400)
        print("Responding...")
        mixer.music.load('response.mp3')
        mixer.music.play()
        while mixer.music.get_busy() == True:
            time.sleep(0.1)
        mixer.music.stop()

        hardware_1.output_update(channel2_status)

        [music_status, playing_number] = music_func.play_music(channel1, music_lists, music_status, playing_number)



    hardware_1.hardware_close()


main()
