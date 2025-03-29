class Room:
    """Represents a room in the hotel."""

    def __init__(self, room_number, room_type, amenities, price_per_night):
        # Initialize room details
        self.__room_number = room_number        # Unique room number
        self.__room_type = room_type            # Type: Single, Double, Suite
        self.__amenities = amenities            # List of amenities
        self.__price_per_night = price_per_night  # Cost per night
        self.__is_available = True              # Availability status

    def get_room_number(self): return self.__room_number  # Return room number
    def get_room_type(self): return self.__room_type      # Return room type
    def get_amenities(self): return self.__amenities      # Return amenities
    def get_price_per_night(self): return self.__price_per_night  # Return price
    def is_available(self): return self.__is_available    # Return availability
    def set_availability(self, status): self.__is_available = status  # Set availability

    def __str__(self):
        # Return a string summary of the room
        return f"Room {self.__room_number} - {self.__room_type} - AED{self.__price_per_night} - Available: {self.__is_available}"
