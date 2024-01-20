import pygame
from pygame import mixer
from gtts import gTTS

# Văn bản cần chuyển đổi 
text = "Xin chào các bạn, mình là trợ lý ảo!"

# Tạo audio từ text
speech = gTTS(text = text, lang='vi')
speech.save("speech.mp3")

# Khởi tạo pygame
pygame.init() 

# Tải file âm thanh MP3
mixer.music.load("speech.mp3")

# Phát âm thanh
mixer.music.play() 

# Chờ phát xong
while mixer.music.get_busy():
    pygame.time.Clock().tick(10)
