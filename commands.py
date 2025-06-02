# commands.py

WAKE_WORD = "python"
TIME = "time"
HELP = "help"
RESET = "reset"

STOP_MUSIC = "stop"
PAUSE_MUSIC = "pause"
RESUME_MUSIC = "resume"
PLAY_MUSIC = "play"
START_PLAYING = "start playing"
GO_BACK_5 = "go back five seconds"
GO_BACK_10 = "go back ten seconds"
GO_BACK_30 = "go back thirty seconds"
START_AT = "start at"
PLAYING_AT = "playing at"
SHUFFLE_MUSIC = "shuffle" 


ARTISTS = "list artist"
ALBUMS = "list abums"
GENRES = "list genres"

GOODBYE = "goodbye"
EXIT = "exit"

help_text = "Welcome to help.  To begin, say python then a command.  List of commands are, time, play, stop ... more commands to follow"
seconds_command = ["one," "two", "three", "four", "five", "six","seven", "eight", "nine","ten", "twenty","thirty","fourty","fifty","sixty","ninety"]

def process_command(text, m, s, d):
    text = text.lower().strip()
    words = text.split()

    if PLAY_MUSIC in text or START_PLAYING in text:
        print("🎵 Playing music...")
        m.test_music()  # Test track only

    elif any(word in words for word in [START_AT, PLAYING_AT]):
        for word in words:
            if word.isdigit():
                print(f"⏩ Starting at {word} seconds")
                m.start_at(int(word))

    elif SHUFFLE_MUSIC in text:
        print("🔀 Shuffling music...")
        m.shuffle()

    elif STOP_MUSIC in text:
        print("⏹️ Stopping music...")
        m.stop_track()

    elif PAUSE_MUSIC in text or RESUME_MUSIC in text:
        print("⏯️ Toggling pause/resume...")
        m.pause_resume()

    elif GO_BACK_5 in text:
        print("⏪ Going back 5 seconds...")
        m.go_back_5()

    elif GO_BACK_10 in text:
        print("⏪ Going back 10 seconds...")
        m.go_back_10()

    elif GO_BACK_30 in text:
        print("⏪ Going back 30 seconds...")
        m.go_back_30()

    elif TIME in text:
        now = d.now().strftime("%I:%M %p")
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
        return "exit"

    else:
        print("🤔 Command not recognized.")
