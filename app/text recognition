import speech_recognition as sr
import time
import pyaudio
import numpy as np
import cv2
from PIL import Image, ImageDraw, ImageFont
r = sr.Recognizer()
while True: 
    with sr.Microphone() as source:
        print("Mời bạn nói: ")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio,language="vi-VI")
            print("Bạn -->: {}".format(text))
        except:
            print("Xin lỗi! tôi không nhận được voice!")
        img = np.zeros((200,400,3),np.uint8)
        # img = Image.open("anh.jpg")
        b,g,r,a = 0,255,0,0

        ## Use cv2.FONT_HERSHEY_XXX to write English.
        text = time.strftime("%Y/%m/%d %H:%M:%S %Z", time.localtime()) 
        cv2.putText(img,  text, (50,50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (b,g,r), 1, cv2.LINE_AA)
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
