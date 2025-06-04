#import sounddevice as sd
#import queue
import sys
import json
import numpy
from music_player_script import MusicPlayer
from datetime import datetime
from vosk import Model, KaldiRecognizer
from commands import *
from speak import Speak
from file_paths import *
import pygame
import pyaudio

q = queue.Queue()
s = Speak()
m = MusicPlayer(home_music_directory) #Music directory
d = datetime
counter = 0

# Load list of limited command words from JSON file
with open("limited_grammar.json", "r") as f:
    limited_word_list = json.load(f)

# Convert list to JSON-formatted string
limited_word_list_to_str = json.dumps(limited_word_list)

# Load the Vosk model
model = Model(model_file_path)
recognizer = KaldiRecognizer(model, 16000, limited_word_list_to_str)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

while True:
    data = stream.read(4000, exception_on_overflow=False)
    if recognizer.AcceptWaveform(data):
        print(json.loads(recognizer.Result()))
    else:
        print(json.loads(recognizer.PartialResult()))


            
