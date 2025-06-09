
from vosk import Model, KaldiRecognizer
from speak import Speak
from listen import *


l = Listen(Model(model_file_path))
s = Speak()

#print intro
print("Wecome to Voice Activated Music Program")
s.speak("Wecome to Voice Activated Music Program")
print("Say, python help for help")



while RUN_LOOP:
    l.listening()
