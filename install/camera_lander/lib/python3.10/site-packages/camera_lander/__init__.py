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

#if gtts doesnt work then comment out 
right = gTTS(text=goRight, lang=language, slow=False) 
left = gTTS(text=goLeft, lang=language, slow=False) 
forward = gTTS(text=goForward, lang=language, slow=False) 
back = gTTS(text=goBack, lang=language, slow=False) 
descend = gTTS(text=goDescend, lang=language, slow=False) 

right.save("right.mp3")
left.save("left.mp3")
forward.save("forward.mp3")
back.save("back.mp3")
descend.save("descend.mp3")





sound = pygame.mixer.Sound("output.wav")

pygame.mixer.music.load("sounds/descend.mp3")
pygame.mixer.music.play()

time.sleep(3)
