from threading import Timer
from pygame import mixer
import time

tomato_count = 0
study_count = 0
relax_count = 0
t0 = Timer(0, None)
#mixer.init()

def tomato_clk(msg, starttime):
    global tomato_count, study_count, relax_count, t0
    tomato_count += 1
    if tomato_count < 7:
        if tomato_count % 2 == 0:
            study_count += 1
            print("Time to study. <", study_count, ">  (from tomato clock)")
            mixer.music.load('sound/tomato_sound_1.mp3')
            mixer.music.play()
            t0 = Timer(16, tomato_clk, ('%d' % (tomato_count), time.time()))
            t0.start()
        else:
            relax_count += 1
            print("Time to relax. <", relax_count, ">  (from tomato clock)")
            mixer.music.load('sound/tomato_sound_2.mp3')
            mixer.music.play()
            t0 = Timer(14, tomato_clk, ('%d' % (tomato_count), time.time()))
            t0.start()
    elif tomato_count == 7:
        print("Tomato clock closed.")
        mixer.music.load('sound/tomato_sound_3.mp3')
        mixer.music.play()
        

def start():
    global tomato_count, study_count, relax_count, t0
    tomato_count = 0
    study_count = 1
    relax_count = 0
    t0 = Timer(4, ready)
    t0.start()

def ready():
    global tomato_count, study_count, relax_count, t0
    print("Time to study. <", study_count, ">  (from tomato clock)")
    mixer.music.load('sound/tomato_sound_1.mp3')
    mixer.music.play()
    t0 = Timer(16, tomato_clk, ('%d' % (tomato_count), time.time()))
    t0.start()

def end():
    global t0
    t0.cancel()

