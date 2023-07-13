import random

class PlaylistGenerator:
    def __init__(self, songs):
        self.songs = songs

    def generate_playlist(self, num_songs=None):
        if num_songs is None or num_songs > len(self.songs):
            num_songs = len(self.songs)
        
        playlist = random.sample(self.songs, num_songs)

        return playlist
    
def main():
    songs = ["song1", "song2", "song3", "song4", "song5", "song6", "song7", "song8", "song9", "song10"]

    generator = PlaylistGenerator(songs)

    playlist = generator.generate_playlist(5)

    print("Your playlist:")
    for song in playlist:
        print(song)

if __name__ == "__main__":
    main()