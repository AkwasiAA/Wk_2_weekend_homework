import unittest
from classes.room import *
from classes.song import *
from classes.guest import *

class TestRoom(unittest.TestCase):

    def SetUp(self):
        self.playlist = [
            Song("Needed Me", "Rhianna", "RnB"),
            Song("Promiscuous", "Nelly Furtado", "Pop"),
            Song("Ms. Jackson", "Outkast", "Rap"),
            Song("Get Down On It", "Kool & The Gang", "Disco")
        ]

        self.room_1 = Room("Room 1", 10)
        self.room_2 = Room("Room 2", 20)
        self.room_3 = Room("Room 3", 25)
        self.room_4 = Room("Room 4", 30)

    def test_room_has_number(self):
        self.assertEqual("Room 1", self.room_1)

    def test_room_has_capacity(self):
        self.assertEqual(10, self.room_1.capacity)

    def test_guest_check_in(self):
        pass

    def test_guest_check_out(self):
        pass

    def test_add_song_to_room(self):
        self.room_1.add_song(self.playlist[1])
        self.assertEqual(2, len(self.room_1.playlist))

