# commands.py
import pygame
import sys

WAKE_WORD = "python"
TIME = "time"
HELP = "help"
RESET = "reset"
RUN_LOOP = True

STOP_MUSIC = "stop"
PAUSE_MUSIC = "pause"
RESUME_MUSIC = "resume"
PLAY_MUSIC = "play"
START_PLAYING = "start playing"
REWIND = "rewind"
GO_BACK_5 = "rewind five seconds"
GO_BACK_10 = "rewind ten seconds"
GO_BACK_30 = "rewind thirty seconds"
SEEK_5 = "seek five seconds"
SEEK_10 = "seek ten seconds"
SEEK_30 = "seek thirty seconds"
START_AT = "start at"
PLAYING_AT = "playing at"
SHUFFLE_MUSIC = "shuffle" 
TEST = "test"


ARTISTS = "list artist"
ALBUMS = "list abums"
GENRES = "list genres"

GOODBYE = "goodbye"
EXIT = "exit"

help_text = "Welcome to help.  To begin, say python then a command.  List of commands are, time, play, stop ... more commands to follow"

def process_command(text, m, s, d):
    text = text.lower().strip()
    words = text.split()
    #print("Words in process_command funciton :", words)

    if pygame.mixer.music.get_busy(): # if the music is playing
        if STOP_MUSIC in text:
            print("⏹️ Stopping music...")
            m.stop_track()

        elif PAUSE_MUSIC in text:
            print("⏯️ Toggling pause/resume...")
            m.pause_resume()

        elif GO_BACK_5 in text:
            print("⏪ Going back 5 seconds...")
            m.move_playhead_func(-5)

        elif GO_BACK_10 in text:
            print("⏪ Going back 10 seconds...")
            m.move_playhead_func(-10)

        elif GO_BACK_30 in text:
            print("⏪ Going back 30 seconds...")
            m.move_playhead_func(-30)

        elif SEEK_5 in text:
            print("⏩ Going forward 5 seconds...")
            m.move_playhead_func(5)

        elif SEEK_10 in text:
            print("⏩ Going forward 10 seconds...")
            m.move_playhead_func(10)

        elif SEEK_30 in text:
            print("⏩ Going forward 30 seconds...")
            m.move_playhead_func(30)

    if TEST in text:
        print("playing test music")
        m.test_music() # Test track only 

    elif RESUME_MUSIC in text:
            print("⏯️ Toggling pause/resume...")
            m.pause_resume()

    elif SHUFFLE_MUSIC in text:
        print("🔀 Shuffling music...")
        m.shuffle()

    elif TIME in text:
        now = d.datetime.now().strftime("%I:%M %p")
        response = f"The current time is {now}"
        print(response)
        s.speak(response)

    elif HELP in text:
        print("📖 Help requested.")
        s.speak(help_text)

    elif RESET in text:
        print("🔄 Resetting recognizer.")
        return "reset"

    elif GOODBYE in text or EXIT in text:
        print("👋 Goodbye!")
        sys.exit()
        #return "exit"

    else:
        print("🤔 Command not recognized.")
