import speech_recognition as sr
import pyaudio
import wave
import time
import numpy as np
import cv2
from PIL import Image, ImageDraw, ImageFont
CHUNK = 1024 
FORMAT = pyaudio.paInt16 #paInt8
CHANNELS = 2 
RATE = 44100 #sample rate
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK) 

print("* recording")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data) 

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()
recognizer = sr.Recognizer()
try:
    with sr.AudioFile(WAVE_OUTPUT_FILENAME) as source:
        audio_data = recognizer.record(source)  # Ghi âm từ tệp

    # Sử dụng Google Web Speech API để nhận dạng giọng nói
    text = recognizer.recognize_google(audio_data,language="vi-VN")

    print("Văn bản: " + text)

except sr.UnknownValueError:
    print("Không thể nhận dạng giọng nói")
except sr.RequestError as e:
    print(f"Lỗi kết nối: {e}")
img = np.zeros((200,400,3),np.uint8)
# img = Image.open("anh.jpg")
b,g,r,a = 0,255,0,0
## Use simsum.ttc to write Chinese.
fontpath = "./BeVietnamPro-Black.ttf"
font = ImageFont.truetype(fontpath, 32)
img_pil = Image.fromarray(img)
draw = ImageDraw.Draw(img_pil)
draw.text((50, 80),  text, font = font, fill = (b, g, r, a))
img = np.array(img_pil)
## Display 
cv2.imshow("res", img)
time.sleep(len(text)*0.1)
img_pil = Image.fromarray(img)
draw = ImageDraw.Draw(img_pil)
draw.text((50, 80),  "", font = font, fill = (b, g, r, a))
cv2.waitKey()
cv2.destroyAllWindows()
