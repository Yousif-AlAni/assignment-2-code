# Final Testable Version with Full Input Validations & Exception Handling

from datetime import datetime
import re

# ------------------- Classes -------------------

# Class representing a room in the hotel
class Room:
    """Represents a room in the hotel."""
    def __init__(self, room_number, room_type, amenities, price_per_night):
        self.__room_number = room_number  # Room number (private)
        self.__room_type = room_type      # Room type (Single, Double, Suite)
        self.__amenities = amenities      # List of amenities
        self.__price_per_night = price_per_night  # Cost per night
        self.__is_available = True        # Availability status

    def get_room_number(self): return self.__room_number
    def set_availability(self, status): self.__is_available = status
    def is_available(self): return self.__is_available
    def get_price_per_night(self): return self.__price_per_night

    # String output for room info
    def __str__(self):
        return f"Room {self.__room_number} - {self.__room_type} - AED{self.__price_per_night} - Available: {self.__is_available}"

# Class representing a guest
class Guest:
    """Represents a hotel guest."""
    def __init__(self, name, email, contact):
        self.__name = name                # Guest's name
        self.__email = email              # Guest's email
        self.__contact = contact          # Contact number
        self.__reservations = []          # List of past reservations

    def get_name(self): return self.__name
    def add_reservation(self, reservation): self.__reservations.append(reservation)
    def get_reservation_history(self): return self.__reservations

# Class representing a reservation
class Reservation:
    """Represents a reservation."""
    def __init__(self, guest, room, check_in, check_out):
        self._guest = guest              # Guest object
        self._room = room                # Room object
        self._check_in = check_in        # Check-in date
        self._check_out = check_out      # Check-out date

    def get_guest(self): return self._guest
    def get_room(self): return self._room
    def get_check_in(self): return self._check_in
    def get_check_out(self): return self._check_out

    # String output for reservation
    def __str__(self):
        return f"Reservation: {self._guest.get_name()} in Room {self._room.get_room_number()} from {self._check_in} to {self._check_out}"

# Class representing an invoice
class Invoice:
    """Generates an invoice for a reservation."""
    def __init__(self, reservation, charges=50, discount=20):
        self.__reservation = reservation  # Associated reservation
        self.__charges = charges          # Extra charges
        self.__discount = discount        # Discount

    # Total cost = nights * price + charges - discount
    def calculate_total(self):
        nights = (self.__reservation.get_check_out() - self.__reservation.get_check_in()).days
        return nights * self.__reservation.get_room().get_price_per_night() + self.__charges - self.__discount

    # String output for invoice
    def __str__(self):
        return f"Invoice for {self.__reservation.get_guest().get_name()}: AED{self.calculate_total()}"

# Class representing a service request (e.g., housekeeping)
class ServiceRequest:
    """Tracks a service request from a guest."""
    def __init__(self, guest, service_type):
        self._guest = guest
        self.__service_type = service_type
        self.__status = "Pending"  # Default status

    def mark_completed(self): self.__status = "Completed"
    def __str__(self): return f"Service Request: {self.__service_type} for {self._guest.get_name()} - Status: {self.__status}"

# Class representing feedback from a guest
class Feedback:
    """Stores guest feedback."""
    def __init__(self, guest, rating, comments):
        self._guest = guest
        self.__rating = rating          # Rating out of 5
        self.__comments = comments      # Feedback text

    def __str__(self):
        return f"Feedback from {self._guest.get_name()}: {self.__rating}/5 - {self.__comments}"

# ------------------- Helper Functions -------------------

# Get and validate date from user input
def input_date(prompt):
    while True:
        try:
            date_input = input(prompt)
            return datetime.strptime(date_input, "%Y-%m-%d").date()
        except ValueError:
            print("❌ Invalid date format. Please use YYYY-MM-DD.")

# General input validator function
def input_validated(prompt, condition_fn, error_msg):
    while True:
        value = input(prompt)
        if condition_fn(value):
            return value
        print(f"❌ {error_msg}")

# Name validation: only letters and spaces
def is_valid_name(name): return name.replace(" ", "").isalpha()
# Email validation using regex
def is_valid_email(email): return bool(re.match(r'^[^@\s]+@[^@\s]+\.[^@\s]+$', email))
# Phone number validation: digits only, at least 10
def is_valid_phone(phone): return phone.isdigit() and len(phone) >= 10
# Rating must be a digit between 1 and 5
def is_valid_rating(r): return r.isdigit() and 1 <= int(r) <= 5

# ------------------- Main Test Function -------------------

def run_test():
    print("\n🏨 Welcome to Royal Stay Hotel 🏨")

    # Get guest details
    name = input_validated("Enter guest name: ", is_valid_name, "Name must contain only letters.")
    email = input_validated("Enter guest email: ", is_valid_email, "Invalid email format.")
    phone = input_validated("Enter contact number: ", is_valid_phone, "Phone must be numeric and at least 10 digits.")

    # Create guest object
    guest = Guest(name, email, phone)

    # Available rooms in the hotel
    rooms = [
        Room(101, "Single", ["Wi-Fi", "TV"], 300),
        Room(102, "Double", ["Wi-Fi", "Mini-Bar"], 450),
        Room(201, "Suite", ["Wi-Fi", "Jacuzzi"], 800)
    ]

    # Display available rooms
    print("\n🛏️ Available Rooms:")
    for r in rooms:
        if r.is_available():
            print(r)

    # Select room with proper validation
    while True:
        room_input = input("\nEnter room number to book: ").strip()
        if not room_input or not room_input.isdigit():
            print("❌ Please enter a valid numeric room number.")
            continue
        room_number = int(room_input)
        selected_room = next((r for r in rooms if r.get_room_number() == room_number and r.is_available()), None)
        if selected_room:
            break
        print("❌ Selected room is not available or does not exist.")

    # Enter and validate check-in and check-out dates
    while True:
        check_in = input_date("Enter check-in date (YYYY-MM-DD): ")
        check_out = input_date("Enter check-out date (YYYY-MM-DD): ")
        if check_out <= check_in:
            print("❌ Check-out date must be after check-in date.")
        else:
            break

    # Create reservation and update room availability
    reservation = Reservation(guest, selected_room, check_in, check_out)
    guest.add_reservation(reservation)
    selected_room.set_availability(False)
    print("\n✅ Reservation Confirmed:", reservation)

    # Create and show invoice
    invoice = Invoice(reservation)
    print("\n🧾 Invoice:")
    print(invoice)

    # Request extra service from guest
    service_type = input_validated("Enter service needed (e.g., Housekeeping): ", lambda s: len(s.strip()) > 0, "Service cannot be empty.")
    service = ServiceRequest(guest, service_type)
    print(service)
    service.mark_completed()
    print("After completion:", service)

    # Collect guest feedback
    rating_input = input_validated("Rate your stay (1-5): ", is_valid_rating, "Rating must be a number between 1 and 5.")
    comment = input("Leave a comment: ")
    feedback = Feedback(guest, int(rating_input), comment)
    print("\n🗣️ Feedback received:")
    print(feedback)

# Run the program
if __name__ == '__main__':
    run_test()
