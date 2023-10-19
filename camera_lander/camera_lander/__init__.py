import pygame 
from gtts import gTTS
import os 
from pathlib import Path 
import time 

pygame.init()
pygame.mixer.init()

goRight = 'go right'
goLeft = 'go left'
goForward = 'go forward'
goBack = 'go back'
goDescend = 'Descend'

language = 'en'

sounds_dir_path = "src/AprilTag-ROS-2/camera_lander/resource/sounds/"

#if gtts doesnt work then comment out 
right = gTTS(text=goRight, lang=language, slow=False) 
left = gTTS(text=goLeft, lang=language, slow=False) 
forward = gTTS(text=goForward, lang=language, slow=False) 
back = gTTS(text=goBack, lang=language, slow=False) 
descend = gTTS(text=goDescend, lang=language, slow=False) 

right.save(sounds_dir_path + "right.mp3")
left.save(sounds_dir_path + "left.mp3")
forward.save(sounds_dir_path + "forward.mp3")
back.save("sounds_dir_path + back.mp3")
descend.save(sounds_dir_path + "descend.mp3")





# sound = pygame.mixer.Sound("output.wav")

pygame.mixer.music.load(sounds_dir_path + "descend.mp3")
pygame.mixer.music.play()

time.sleep(3)
