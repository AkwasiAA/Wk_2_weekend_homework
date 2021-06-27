import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.song = Song("Needed Me", "Rhianna", "RnB")

    def test_song_has_title(self):
        self.assertEqual("Needed Me", self.song.title)

    def test_song_has_artist(self):
        self.assertEqual("Rhianna", self.song.artist)

    def test_song_has_genre(self):
        self.assertEqual("RnB", self.song.genre)