import pygame
import os
import time
import random
from file_paths import *
from speak import Speak

s = Speak()

class MusicPlayer:

    def __init__(self, music_directory):
        self.music_directory = music_directory
        self.supported_extensions = ('.mp3', '.m4a', '.mv4')  # Added m4a
        self.shuffle_song_list = []
        self.played_song_list = []
        self.paused = False

    pygame.mixer.init()
    current_track = 0
    heard_wake_word = False
    

    def test_music(self):
        pygame.mixer.music.load(test_song)
        s.speak(os.path.basename(test_song))
        time.sleep(3)
        pygame.mixer.music.play()

    '''
    def play_track(index):
        pygame.mixer.music.load(playlist[index])
        pygame.mixer.music.play()
        print(f"Now playing: {os.path.basename(playlist[index])}")
    '''
    def play(self, music):
        if music is track:
            #do someting
            pass
        if music is album:
            #do somehitng
            pass
        if music is artist:
            #do something
            pass
            
    def stop_track(self):
        pygame.mixer.music.stop()
        print("Playback stopped.")

    def pause_resume(self):
        
        if self.paused:
            pygame.mixer.music.unpause()
            print("Resumed.")
        else:
            pygame.mixer.music.pause()
            print("Paused.")
        self.paused = True

    def go_back_5(self):
        current_pos = pygame.mixer.music.get_pos() / 1000  # ms to sec
        new_pos = max(0, current_pos - 5)
        pygame.mixer.music.play(start=new_pos)
        print(f"Jumped to {int(new_pos)} seconds.")

    def go_back_10(self):
        current_pos = pygame.mixer.music.get_pos() / 1000  # ms to sec
        new_pos = max(0, current_pos - 10)
        pygame.mixer.music.play(start=new_pos)
        print(f"Jumped to {int(new_pos)} seconds.")

    def go_back_30(self):
        current_pos = pygame.mixer.music.get_pos() / 1000  # ms to sec
        new_pos = max(0, current_pos - 30)
        pygame.mixer.music.play(start=new_pos)
        print(f"Jumped to {int(new_pos)} seconds.")

    def start_at(self,seconds):
        #current_pos = pygame.mixer.music.get_pos() / 1000  # ms to sec
        #new_pos = max(0, current_pos + seconds)
        convert_to_miliseconds = seconds * 1000
        pygame.mixer.music.play(start=convert_to_miliseconds)
        print(f"Jumped to {int(seconds)} seconds.")

    def duck_volume(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.set_volume(0.3)
            print("Volume dropped")
            time.sleep(5)
            pygame.mixer.music.set_volume(1.0)
        pass

    def shuffle(self):

        # Recursively walk through directory and find music files
        for root, dirs, files in os.walk(self.music_directory):
            for file in files:                                  
                print(f"file {file}")
                if file.lower().endswith(self.supported_extensions):
                    print(f"adding {os.path.join(root, file)}")
                    self.shuffle_song_list.append(os.path.join(root, file))
        for song in self.shuffle_song_list:
            print("Shufled song list.......")
            print(song)

        if not self.shuffle_song_list:
            raise FileNotFoundError(f"No music files found in {self.music_directory}")

        self.played_song_list = []

        while True:
            if len(self.played_song_list) == len(self.shuffle_song_list):
                print("All songs have been played. Restarting shuffle.")
                self.played_song_list = []

            remaining_songs = [song for song in self.shuffle_song_list if song not in self.played_song_list]
            print(f"remaining_songs {remaining_songs}")

            next_song = random.choice(remaining_songs)
            print(f"next song: {next_song}")
            next_song = str(next_song)
            pygame.mixer.music.load(next_song)
            pygame.mixer.music.play()
            #self.play_song(next_song)
            #self.played_song_list.append(next_song)
            print(f"adding to played song list: {self.played_song_list}")
            # Wait until the music stops playing
            while pygame.mixer.music.get_busy():
                time.sleep(0.1)  # Prevent high CPU usage

    def play_song(self, song_path):
        print(f"Now playing: {os.path.basename(song_path)}")  # Stub for actual playback
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play()
        

'''
def seek(seconds):
    current_pos = pygame.mixer.music.get_pos() / 1000  # ms to sec
    new_pos = max(0, current_pos + seconds)
    pygame.mixer.music.play(start=new_pos)
    print(f"Jumped to {int(new_pos)} seconds.")

def next_track():
    global current_track
    current_track = (current_track + 1) % len(playlist)
    play_track(current_track)

def previous_track():
    global current_track
    current_track = (current_track - 1) % len(playlist)
    play_track(current_track)

# Start playing the first track
play_track(current_track)

# Command loop
while True:
    command = input("\nCommand: ").lower()
    if "pause" in command:
        pause_resume()
    elif "stop" in command:
        stop_track()
    elif "resume" in command:
        pause_resume()
    elif "forward 10" in command:
        seek(10)
    elif "back 10" in command:
        seek(-10)
    elif "forward 5" in command:
        seek(5)
    elif "back 5" in command:
        seek(-5)
    elif "next" in command:
        next_track()
    elif "previous" in command:
        previous_track()
    elif "quit" in command:
        stop_track()
        print("Goodbye.")
        break
    else:
        print("Unknown command.")
'''