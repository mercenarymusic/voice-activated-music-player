import sounddevice as sd
import queue
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

q = queue.Queue()
s = Speak()
m = MusicPlayer(home_music_directory) #Music directory
d = datetime
counter = 0


# Callback pushes audio data to the queue
def callback(indata, frames, time, status):
    if status:
        print("Audio callback error:", status, file=sys.stderr)
    q.put(indata.copy())  #use .copy() to avoid buffer issues

# Load the Vosk model
model = Model("/home/phaser/workspace/github.com/mercenarymusic/make_python_talk/ch03/vosk-model-en-us-0.22-lgraph")
recognizer = KaldiRecognizer(model, 16000)

# Start the stream
with sd.InputStream(samplerate=16000, channels=1, dtype='int16',
                    blocksize=8000, callback=callback):
    print("🎤 Speak now... (Ctrl+C to stop)")
    
    #test espeak
    s.speak("test sentence.")
    
    while True:
        if s.is_not_speaking:
            data = q.get()
            sentence = ""
            if counter == 50:
                result = recognizer.Reset()
                counter = 0
            if recognizer.AcceptWaveform(data.tobytes()):
                result = json.loads(recognizer.Result())
                text = result["text"].lower().strip()
                print("You said:", result["text"])
                result = recognizer.Reset()
                if WAKE_WORD in text:
                    print("Wake word detected. I'm listening...")
                    m.duck_volume()
                    for seconds in text:
                        if seconds in seconds_command:
                            print("saying seconds", seconds)
                    if PLAY_MUSIC in text or START_PLAYING in text:
                        print("Playing music...")
                        m.test_music() # test track only 
                    if START_AT in text or PLAYING_AT:
                        for seconds in text:
                            if seconds.isdigit():
                                print(f"{seconds} is a digit")
                                print(f"Starting at {seconds}")
                                m.start_at(seconds)
                    if SHUFFLE_MUSIC in text:
                        m.shuffle()
                    if STOP_MUSIC in text:
                        m.stop_track()
                    if PAUSE_MUSIC in text or RESUME_MUSIC in text:
                        m.pause_resume()
                    if GO_BACK_5 in text:
                        m.go_back_5()
                    if GO_BACK_10 in text:
                        m.go_back_10()
                    if GO_BACK_30 in text:
                        m.go_back_30()
                    if TIME in text:
                        now = datetime.now().strftime("%I:%M %p")
                        print(f"The current time is {now}")
                        time = f"The current time is {now}"
                        s.speak(time)
                    if HELP in text:
                        s.speak(help_text)
                    if  RESET in text:
                        print("Resetting")
                        #result = recognizer.Reset()
                        q.task_done()
                        counter = 0
                    if GOODBYE in text or EXIT in text:
                        print("Goodbye!")
                        break
                

            else:
                partial = json.loads(recognizer.PartialResult())
                #print("Partial:", partial["partial"])
                counter += 1
                #print(counter)
               
        else:
            q.get()  # Still consume the queue to prevent blocking, just discard
        

