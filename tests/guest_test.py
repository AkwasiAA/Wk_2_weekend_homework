import unittest
from classes.guest import *
from classes.song import *

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Lydia", "Room 1", self.promiscuous)
        self.promiscuous = Song("Promiscuous", "Nelly Furtado", "Pop")

    def test_guest_has_name(self):
        self.assertEqual("Lydia", self.guest.name)

    def test_guest_has_booking(self):
        self.assertEqual("Room 1", self.guest.room_number_booked)

    def test_guest_has_favourite_song(self):
        self.assertEqual(self.promiscuous, self.guest.favourite_song)

    def test_fav_song_is_on_playlist(self):
        pass