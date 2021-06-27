class Guest:

    def __init__(self, name, room_number_booked, favourite_song):
        self.name = name
        self.room_number_booked = room_number_booked
        self.favourite_song = favourite_song

    def fav_song(self, playlist):
        if self.favourite_song in playlist:
            return f"Whoo this is my favourite song!!"