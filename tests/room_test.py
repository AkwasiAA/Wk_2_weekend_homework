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
        self.room = Room("Room 1", 15)
        # self.room = Room("Room 2", 20)
        # self.room = Room("Room 3", 25)
        # self.room = Room("Room 4", 30)

        self.guest_1 =  Guest("Andy","Room 2", "Ms Jackson")

    def test_room_has_number(self):
        self.assertEqual("Room 1", self.room.room_number)

    def test_room_has_capacity(self):
        self.assertEqual(15, self.room.capacity)

    def test_guest_check_in(self):
        self.room.check_in_guest(self.guest_1)
        self.assertEqual(1, len(self.room.guest))

    def test_guest_check_out(self):
        self.room.check_in_guest(self.guest_1)
        self.room.check_out_guest(self.guest_1)
        self.assertEqual(0, len(self.room.guest))

    def test_add_song_to_room(self):
        self.room_1.add_song(self.playlist[1])
        self.assertEqual(2, len(self.room.playlist))

