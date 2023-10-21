import pygame 
from gtts import gTTS
import os 
from pathlib import Path 
import time 

# Google TTS setup
sounds_dir_path = "src/AprilTag-ROS-2/camera_lander/resource/sounds/"
language = 'en'

# generate TTS sound snippets
voice_snippets = {'right':   'go right',
                  'left':    'go left',
                  'back':    'go back',
                  'forward': 'go forward',
                  'descend': 'descend'
                 }

for name, text in voice_snippets.items():
    sound = gTTS(text=text, lang=language, slow=False)
    sound.save(sounds_dir_path + name + ".mp3")

# Initialize PyGame for playing sounds
pygame.init()
pygame.mixer.init()
# pygame.mixer.music.load(sounds_dir_path + "descend.mp3")
# pygame.mixer.music.play()

time.sleep(3)
