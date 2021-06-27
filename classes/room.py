class Room:

    def __init__(self, room_number, capacity):
        self.room_number = room_number
        self.capacity = capacity

        self.price = price
        self.guestlist = []
        self.playlist = []

    def check_in_guest(self, guest):
        if len(self.guestlist) < self.capacity:
            self.guestlist.append(guest)
        else:
            print("Unfortunately this room is currently full")

    def check_out_guest(self, guest):
        self.guestlist.remove(guest)

    def add_songs(self, song):
        self.playlist.append(song)

   

   