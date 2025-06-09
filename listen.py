import json
import numpy
import datetime
from vosk import Model, KaldiRecognizer
import pygame
import pyaudio
from file_paths import *
from commands import *
from speak import Speak
from music_player_script import MusicPlayer


class Listen:

    def __init__(self, model):

        self.s = Speak()
        self.p = pyaudio.PyAudio()
        self.m = MusicPlayer(home_music_directory) #Music directory
        self.d = datetime
        # Load limited words
        with open("limited_grammar.json", "r") as f:
            limited_word_list = json.load(f)
        limited_word_list_to_str = json.dumps(limited_word_list)

        self.recognizer = KaldiRecognizer(model, 16000, limited_word_list_to_str)
        self.model = model

        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
        self.stream.start_stream()

        self.count = 0
        self.previous_result = ""
        self.current_result = ""
 

    def listening(self):
        data = self.stream.read(4000, exception_on_overflow=False)
        #if pygame.mixer.music.get_busy(): # get track position for debugging 
        #    print(pygame.mixer.music.get_pos())
        if self.recognizer.AcceptWaveform(data):
            the_program_heard = json.loads(self.recognizer.Result()).get("text")
            spoken_words_list = []
            for word in the_program_heard.split():
                if word == WAKE_WORD:
                    print("heard wake word")
                    process_command(the_program_heard, self.m,self.s,self.d)
                if word == GOODBYE or word == EXIT:
                    RUN_LOOP = False
        else:
            self.count += 1
            #print(json.loads(self.recognizer.PartialResult()))
            current_result = json.loads(self.recognizer.PartialResult())
            if  current_result.get("result") is not None and self.current_result == self.previous_result: # prevent feedback loop
                self.recognizer.Reset()
                previous_result = current_result
                print("resetting current recognizer...")
            '''
            if self.count >= 30:
                self.recognizer.Reset()
                print("resetting recognizer...")
                self.count = 0  # reset counter

  '''