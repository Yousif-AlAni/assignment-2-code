class Feedback:
    """Stores guest feedback."""

    def __init__(self, guest, rating, comments):
        # Initialize feedback details
        self._guest = guest
        self.__rating = rating          # Rating out of 5
        self.__comments = comments      # Feedback comment

    def __str__(self):
        # Return feedback summary
        return f"Feedback from {self._guest.get_name()}: {self.__rating}/5 - {self.__comments}"
