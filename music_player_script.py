import pygame
import os
import time
import random
import threading
import re #regualr expressions
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
        self.move_playhead = 0

    pygame.mixer.init()
    heard_wake_word = False
    

    def play(self,song_path):
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play()

    def test_music(self):
        pygame.mixer.music.load(test_song)
        s.speak(os.path.basename(test_song))
        time.sleep(3)
        self.play(test_song)
            
    def stop_track(self):
        pygame.mixer.music.stop()
        print("Playback stopped.")

    def pause_resume(self):
        
        if self.paused:
            pygame.mixer.music.unpause()
            print("Resumed.")
            self.paused = False
        else:
            pygame.mixer.music.pause()
            print("Paused.")
            self.paused = True
    
    def track_time(self):
        tracking_time = int(time.time() * 1000)
        print(tracking_time)
        self.elapsed_time = self.new_track_position + tracking_time
        print("elapsed time in track time. ", self.elapsed_time)

    def move_playhead_func(self, rewind_time): # takes a +/- number
        track_position = pygame.mixer.music.get_pos() / 1000
        track_position += self.move_playhead  # if the playhead isn't zero adjust track position to playhead
        track_position += rewind_time # subtrack / add time from playhead
        pygame.mixer.music.play(start=int(track_position)) # start playback at new track position
        print("Track position: ", int(track_position))
        self.move_playhead = track_position # update playhead


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
        '''
        for song in self.shuffle_song_list:
            print("Shufled song list.......")
            print(song)
        '''
        if not self.shuffle_song_list:
            raise FileNotFoundError(f"No music files found in {self.music_directory}")

        self.played_song_list = []

        def play_loop():
            while True:
                if not pygame.mixer.music.get_busy() or not self.paused: # if music isn't playing and not paused

                    remaining_songs = []
                    for song in self.shuffle_song_list:
                        if song not in self.played_song_list:
                            remaining_songs.append(song)

                    next_song = random.choice(remaining_songs)
                    print(f"next song: {self.extract_filename(str(next_song))}")
                    s.speak(os.path.basename(self.extract_filename(str(next_song))))
                    self.played_song_list.append(next_song)
                    self.play(next_song)  # calls blocking function above

        threading.Thread(target=play_loop, daemon=True).start()

    def extract_filename(self, file_path):
        # convert file_path to string when calling this function
        match = re.search(r"[^/]+$", file_path)
        if match:
            return match.group(0)
        return None
    

