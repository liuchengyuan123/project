import requests
import json
import base64
import os
import time
from pyaudio import PyAudio, paInt16
import wave

RATE = "16000"
FORMAT = "wav"
CUID="wate_play"
DEV_PID="1536"

framerate=16000
NUM_SAMPLES=2000
channels=1
sampwidth=2
TIME=2

def get_token():
	#获取tokent
	baidu_server = "https://openapi.baidu.com/oauth/2.0/token?"
	grant_type = "client_credentials"
	#API Key
	client_id = "E24VAQZPYVoA2rkRg3S8d5y7"
	#Secret Key
	client_secret = "u1YDBspiHgF9ggbYP6z43VZ4dPklYE7e" 

	#拼url
	url ="%sgrant_type=%s&client_id=%s&client_secret=%s"%(baidu_server,grant_type,client_id,client_secret)
	print(url)
	#获取token
	res = requests.post(url)
	print(res.text)
	token = json.loads(res.text)["access_token"]
	print(token)
	return token

def get_word(filename, token):
	#设置格式
#	RATE = "16000"
#	FORMAT = "amr"
#	CUID="wate_play"
#	DEV_PID="1536"
	#以字节格式读取文件之后进行编码
	with open(filename, "rb") as f:
	    speech = base64.b64encode(f.read()).decode('utf8')
	size = os.path.getsize(filename)
	headers = { 'Content-Type' : 'application/json'}
	url = "https://vop.baidu.com/server_api"
	data = {
		"format":FORMAT,
		"rate":RATE,
		"dev_pid":DEV_PID,
		"speech":speech,
		"cuid":CUID,
		"len":size,
		"channel":1,
		"token":token
	}
	req = requests.post(url,json.dumps(data),headers)
	result = json.loads(req.text)
	print('we get:')
	print(result["result"][0])
	return result

def save_wav_file(filename, data):
	'''save the data to the wavfile'''
	wf = wave.open(filename, "wb")
	wf.setnchannels(channels)
	wf.setsampwidth(sampwidth)
	wf.setframerate(framerate)
	wf.writeframes(b"".join(data))
	wf.close()

def my_record(filename):
	pa = PyAudio()
#	stream = pa.open(format = paInt16, channels=1, rate=framerate, input=True, frames_pre_buffer=NUM_SAMPLES)
	stream = pa.open(format = paInt16, channels=1, rate=framerate, input=True)
	my_buf = []
	count = 0
	print('.')
	while count < TIME * 10:
		string_audio_data = stream.read(NUM_SAMPLES)
		my_buf.append(string_audio_data)
		count += 1
	save_wav_file(filename, my_buf)
	stream.close()

chunk = 2014

def play(filename):
	wf = wave.open(filename, 'rb')
	p = PyAudio()
	stream = p.open(format=p.get_format_from_width(wf.getsampwidth(), channels=
				wf.getnchannels(), rate=wf.getframerate(), output=True))
	while True:
		data = wf.readframes(chunk)
		if data == "":
			break
		stream.write(data)
	stream.cloase()
	p.terminate()

if __name__ == '__main__':
	'''
	while True:
		time.sleep(5)
		print('start recording')
		my_record('1.wav')
		token = get_token()
		try:
			ret = get_word('1.wav', token)
		except Exception as e:
			print(e)
#print(ret)
	'''
	filename = '1.wav'
	print("let's talk")
	my_record(filename)
	token = get_token()
	ret = get_word(filename, token)
