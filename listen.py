import sounddevice as sd
import queue
import sys
import json
import numpy
from vosk import Model, KaldiRecognizer
import pygame


class Listen:

    q = queue.Q()

    def __init__(self, KaldiRecognizer);
        self.data = q.get()
        self.recognizer = KaldiRecognizer()

    # Callback pushes audio data to the queue
    def callback(indata, frames, time, status):
        if status:
            print("Audio callback error:", status, file=sys.stderr)
        q.put(indata.copy())  #use .copy() to avoid buffer issues

    # Load the Vosk model
    model = Model("/home/phaser/workspace/github.com/mercenarymusic/make_python_talk/ch03/vosk-model-en-us-0.22-lgraph")
    recognizer = KaldiRecognizer(model, 16000)