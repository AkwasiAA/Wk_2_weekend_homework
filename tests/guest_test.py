import unittest
from classes.guest import *
from classes.song import *

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Lydia", "Room 1", "Promiscuous")
        self.favourite_song = Song("Promiscuous", "Nelly Furtado", "Pop")

    def test_guest_has_name(self):
        self.assertEqual("Lydia", self.guest.name)

    def test_guest_has_booking(self):
        self.assertEqual("Room 1", self.guest.room_number_booked)

    # def test_guest_has_favourite_song(self):
    #     # self.assertEqual("Promiscuous", "Nelly Furtado", "Pop", self.favourite_song)
    #     pass

    