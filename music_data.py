class Track:
    def __init__(self, title, artist, album, genre, track_number, disc_number, file_path):
        self.title = title
        self.artist = artist
        self.album = album
        self.genre = genre
        self.track_number = track_number
        self.disc_number = disc_number
        self.file_path = file_path

class Album:
    def __init__(self, title, artist, genre, year):
        self.title = title
        self.artist = artist
        self.genre = genre
        self.year = year
        self.tracks = []  # List[Track]

    def add_track(self, track: Track):
        self.tracks.append(track)

class Artist:
    def __init__(self, name):
        self.name = name
        self.albums = []  # List[Album]

    def add_album(self, album: Album):
        self.albums.append(album)

# Usage examples:
# artist.albums[0].tracks[1].title
'''
artist = Artist("The Beatles")
album = Album("Abbey Road", "Rock", 1969)

album.add_track(Track("Come Together", 1, "4:19"))
album.add_track(Track("Something", 2, "3:03"))

artist.add_album(album)
'''