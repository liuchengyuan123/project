import wave
import numpy as np
import matplotlib.pyplot as plt
from Resize import resize
import speech_recognition as sr
import speech
import pyaudio
import wave
import os
import requests
import json
import base64
import time
from pyaudio import PyAudio, paInt16

'''
declare a class named Recognizer
it charges the part of recognition work under GUI
'''


class Recognizer:

    def __init__(self):
        self.cnt = 0
        self.wav_file_st = 'wavFileNum'
        self.dict = [
            'rich',
            'flash',
            'blog',
            'mathematics',
            'hard',
            'twenty',
            'love',
            'girl',
            'banana',
            'apple'
        ]
        self.keyword = []
        for word in self.dict:
            self.keyword.append((word, 1.0))
        return

    '''
    record speech voice
    return the name of wavfile
    '''
    def record(self, auto_cover):
        if auto_cover is True:
            self.cnt -= 1
        self.cnt += 1
        WAVE_OUTPUT_FILENAME = self.wav_file_st + str(self.cnt) + '.wav'
        # some parameter of recording file
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 2
        RATE = 16000
        RECORD_SECONDS = 2

        p = pyaudio.PyAudio()

        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)
        print("开始录音,请说话......")
        frames = []
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)

        print("录音结束,请闭嘴!")

        stream.stop_stream()
        stream.close()
        p.terminate()
        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
        return WAVE_OUTPUT_FILENAME

    def welcome(self):
        speech.say('欢迎与我交流')

    '''
    from wavfile get mfcc data
    '''
    def get_wav_mfcc(self, wav_path):
        f = wave.open(wav_path, 'rb')
        params = f.getparams()
        # print("params:",params)
        nchannels, sampwidth, framerate, nframes = params[:4]
        strData = f.readframes(nframes) #读取音频，字符串格式
        waveData = np.fromstring(strData, dtype=np.int16) #将字符串转化为int
        waveData = waveData*1.0/(max(abs(waveData))) #wave幅值归一化
        waveData = np.reshape(waveData, [nframes, nchannels]).T
        f.close()
        data = list(np.array(waveData[0]))

        while len(data)>16000:
            # print('len(data)', len(data), len(waveData[0]))
            del data[len(data)-1]
            del data[0]
        # print(len(data))
        while len(data) < 16000:
            data.append(0)
        # print(len(data))

        data = np.array(data)
        # 平方之后，开平方，取正数，值的范围在  0-1  之间
        data = data ** 2
        data = data ** 0.5
        return data

    '''
    package sr will tell which word you were saying
    it returns results which probably be the answer
    method: sphinx
    '''
    def rec_word(self, filename):
        r = sr.Recognizer()
        best = []
        with sr.AudioFile(filename) as source:
            audio = r.record(source)
        try:
            ret = r.recognize_sphinx(audio, keyword_entries=self.keyword)
            print(ret)
            best = [i for i in ret.split()]
        except:
            print('not sure')
        return best

    '''
    plot mfcc_pic, and save to the target png file
    '''
    def plot_save(self, pngf, data):
        plt.clf()
        plt.plot(data)
        plt.savefig('Oldboy.png')
        resize('Oldboy.png')

'''
class only chat
words limited
'''


class Talker:
    def __init__(self):
        self.RATE = "16000"
        self.FORMAT = "wav"
        self.CUID = "wate_play"
        self.DEV_PID = "1536"

        self.framerate = 16000
        self.NUM_SAMPLES = 2000
        self.channels = 1
        self.sampwidth = 2
        self.TIME = 2

        self.wav_file_st = 'kaka'
        self.cnt = 0

    '''
    client: shdxlcy
    '''
    def get_token(self):
        # 获取tokent
        baidu_server = "https://openapi.baidu.com/oauth/2.0/token?"
        grant_type = "client_credentials"
        # API Key
        client_id = "E24VAQZPYVoA2rkRg3S8d5y7"
        # Secret Key
        client_secret = "u1YDBspiHgF9ggbYP6z43VZ4dPklYE7e"

        # 拼url
        url = "%sgrant_type=%s&client_id=%s&client_secret=%s" % (baidu_server, grant_type, client_id, client_secret)
        print(url)
        # 获取token
        res = requests.post(url)
        print(res.text)
        token = json.loads(res.text)["access_token"]
        print(token)
        return token

    '''
    using API -- speech to text
    '''
    def get_word(self, filename, token):
        # 设置格式
        # RATE = "16000"
        # FORMAT = "amr"
        # CUID="wate_play"
        # DEV_PID="1536"
        # 以字节格式读取文件之后进行编码
        with open(filename, "rb") as f:
            tspeech = base64.b64encode(f.read()).decode('utf8')
        size = os.path.getsize(filename)
        headers = {'Content-Type': 'application/json'}
        url = "https://vop.baidu.com/server_api"
        data = {
            "format": self.FORMAT,
            "rate": self.RATE,
            "dev_pid": self.DEV_PID,
            "speech": tspeech,
            "cuid": self.CUID,
            "len": size,
            "channel": 1,
            "token": token
        }
        req = requests.post(url, json.dumps(data), headers)
        result = json.loads(req.text)
        print(result["result"][0])
        return result["result"]

    def save_wav_file(self, filename, data):
        '''save the data to the wavfile'''
        wf = wave.open(filename, "wb")
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.sampwidth)
        wf.setframerate(self.framerate)
        wf.writeframes(b"".join(data))
        wf.close()

    def my_record(self, filename):
        pa = PyAudio()
        # stream = pa.open(format = paInt16, channels=1, rate=framerate, input=True, frames_pre_buffer=NUM_SAMPLES)
        stream = pa.open(format=paInt16, channels=1, rate=self.framerate, input=True)
        my_buf = []
        count = 0
        print('.')
        while count < self.TIME * 10:
            string_audio_data = stream.read(self.NUM_SAMPLES)
            my_buf.append(string_audio_data)
            count += 1
        self.save_wav_file(filename, my_buf)
        stream.close()

    def work(self, cover):
        print('start recording')
        if cover is True:
            self.cnt -= 1
        self.cnt += 1
        name = self.wav_file_st + str(self.cnt) + '.wav'
        self.my_record(name)
        token = self.get_token()
        try:
            ret = self.get_word(name, token)
            return ret, name
        except Exception as e:
            print(e)
            speech.say('我不太明白你在说什么')
        return None
