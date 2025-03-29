class Reservation:
    """Represents a reservation."""

    def __init__(self, guest, room, check_in, check_out):
        # Initialize reservation details
        self._guest = guest            # Guest who made the reservation
        self._room = room              # Room reserved
        self._check_in = check_in      # Check-in date
        self._check_out = check_out    # Check-out date

    def get_guest(self): return self._guest        # Return guest
    def get_room(self): return self._room          # Return room
    def get_check_in(self): return self._check_in  # Return check-in
    def get_check_out(self): return self._check_out  # Return check-out

    def __str__(self):
        # Return reservation summary
        return f"Reservation: {self._guest.get_name()} in Room {self._room.get_room_number()} from {self._check_in} to {self._check_out}"
