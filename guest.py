class Guest:
    """Represents a hotel guest."""

    def __init__(self, name, email, contact):
        # Initialize guest details
        self.__name = name                      # Guest name
        self.__email = email                    # Guest email
        self.__contact = contact                # Guest contact number
        self.__reservations = []                # List of reservations
        self.__loyalty_points = 0               # Loyalty points

    def get_name(self): return self.__name              # Get name
    def get_email(self): return self.__email            # Get email
    def get_contact(self): return self.__contact        # Get contact number
    def get_loyalty_points(self): return self.__loyalty_points  # Get loyalty points

    def set_name(self, name): self.__name = name        # Set name
    def set_email(self, email): self.__email = email    # Set email
    def set_contact(self, contact): self.__contact = contact  # Set contact

    def add_reservation(self, reservation):
        # Add a reservation and increase loyalty points
        self.__reservations.append(reservation)
        self.__loyalty_points += 10

    def get_reservation_history(self): return self.__reservations  # Get all reservations
