

import pyttsx3
import threading

class Speak:
    def __init__(self):
        self.engine = pyttsx3.init(driverName='espeak')
        self.is_not_speaking = True  # default to True

        self.voices = self.engine.getProperty('voices')
        for voice in self.voices:
            if "english-us" in voice.name:
                self.engine.setProperty('voice', voice.id)
                break
        self.engine.setProperty('rate', 175)
        self.engine.setProperty('volume', 1.0)

        self.engine.connect('finished-utterance', self.on_finished)
    
    def on_finished(self, name, completed):
        print("✔️ finished-utterance event fired")
        self.is_not_speaking = True

    def _speak_thread(self, text):
        self.is_not_speaking = False
        print(f"[ENGINE] Speaking: {text}")
        self.engine.say(text)
        self.engine.runAndWait()  # This will block inside the thread

    def threaded_speaking(self, text):
        t = threading.Thread(target=self._speak_thread, args=(text,))
        t.start()

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

