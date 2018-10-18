# -*- coding: utf-8 -*-
###  wav_func.py  ###
###  功能：将USB声音数据转化为wav声音文件  ###
import pyaudio
import wave
import os
import sys
from pydub import AudioSegment  #需要一并安装sox

class Wav():
    def __init__(self):
        self.CHUNK = 512
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE1 = 44100
        self.RATE1_MOD = 49000  #刻意修改波特率以提高音调
        self.RATE2 = 16000
        self.RECORD_SECONDS = 2.5
        self.filepath = "./"
        self.filename1 = "original_sound"
        self.filename2 = "input_sound"
        self.frames = []


    def record_to_wav(self):
        # wav文件写入
        self.frames = []
        print("Recording sound data...")
        p = pyaudio.PyAudio()
        stream = p.open(format=self.FORMAT,
                        channels=self.CHANNELS,
                        rate=self.RATE1,
                        input=True,
                        frames_per_buffer=self.CHUNK)
        
        for i in range(0, int(self.RATE1 / self.CHUNK * self.RECORD_SECONDS)):
            data = stream.read(self.CHUNK, exception_on_overflow=False)  #采样
            self.frames.append(data)
        
        print('Record done.')
        stream.stop_stream()
        stream.close()
        p.terminate()

        outfile = self.filepath + self.filename1 + ".wav"
        wf = wave.open(outfile, 'wb')  #定义存储路径以及文件名
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE1_MOD)
        wf.writeframes(b''.join(self.frames))
        wf.close()
        
        #音量增大和采样率修改
        convfile = self.filepath + self.filename2 + ".wav"
        sound1 = AudioSegment.from_file(outfile, format="wav")
        sound1 = sound1.remove_dc_offset()  #消除直流偏移
        sound1 = sound1.invert_phase()  #消除反相波
        sound1 = sound1 + 35  #音量增大35dB
        sound2 = sound1.set_frame_rate(self.RATE2)
        sound2.export(convfile, format="wav")

