# Final Testable Version with Full Input Validations & Exception Handling

from datetime import datetime
import re

# ------------------- Classes -------------------

class Room:
    """Represents a room in the hotel."""
    def __init__(self, room_number, room_type, amenities, price_per_night):
        self.__room_number = room_number
        self.__room_type = room_type
        self.__amenities = amenities
        self.__price_per_night = price_per_night
        self.__is_available = True

    def get_room_number(self): return self.__room_number
    def set_availability(self, status): self.__is_available = status
    def is_available(self): return self.__is_available
    def get_price_per_night(self): return self.__price_per_night
    def __str__(self):
        return f"Room {self.__room_number} - {self.__room_type} - AED{self.__price_per_night} - Available: {self.__is_available}"

class Guest:
    """Represents a hotel guest."""
    def __init__(self, name, email, contact):
        self.__name = name
        self.__email = email
        self.__contact = contact
        self.__reservations = []

    def get_name(self): return self.__name
    def add_reservation(self, reservation): self.__reservations.append(reservation)
    def get_reservation_history(self): return self.__reservations

class Reservation:
    """Represents a reservation."""
    def __init__(self, guest, room, check_in, check_out):
        self._guest = guest
        self._room = room
        self._check_in = check_in
        self._check_out = check_out

    def get_guest(self): return self._guest
    def get_room(self): return self._room
    def get_check_in(self): return self._check_in
    def get_check_out(self): return self._check_out
    def __str__(self):
        return f"Reservation: {self._guest.get_name()} in Room {self._room.get_room_number()} from {self._check_in} to {self._check_out}"

class Invoice:
    """Generates an invoice for a reservation."""
    def __init__(self, reservation, charges=50, discount=20):
        self.__reservation = reservation
        self.__charges = charges
        self.__discount = discount

    def calculate_total(self):
        nights = (self.__reservation.get_check_out() - self.__reservation.get_check_in()).days
        return nights * self.__reservation.get_room().get_price_per_night() + self.__charges - self.__discount

    def __str__(self):
        return f"Invoice for {self.__reservation.get_guest().get_name()}: AED{self.calculate_total()}"

class ServiceRequest:
    """Tracks a service request from a guest."""
    def __init__(self, guest, service_type):
        self._guest = guest
        self.__service_type = service_type
        self.__status = "Pending"

    def mark_completed(self): self.__status = "Completed"
    def __str__(self): return f"Service Request: {self.__service_type} for {self._guest.get_name()} - Status: {self.__status}"

class Feedback:
    """Stores guest feedback."""
    def __init__(self, guest, rating, comments):
        self._guest = guest
        self.__rating = rating
        self.__comments = comments

    def __str__(self):
        return f"Feedback from {self._guest.get_name()}: {self.__rating}/5 - {self.__comments}"

# ------------------- Helper Functions -------------------

def input_date(prompt):
    while True:
        try:
            date_input = input(prompt)
            return datetime.strptime(date_input, "%Y-%m-%d").date()
        except ValueError:
            print("❌ Invalid date format. Please use YYYY-MM-DD.")

def input_validated(prompt, condition_fn, error_msg):
    while True:
        value = input(prompt)
        if condition_fn(value):
            return value
        print(f"❌ {error_msg}")

def is_valid_name(name): return name.replace(" ", "").isalpha()
def is_valid_email(email): return bool(re.match(r'^[^@\s]+@[^@\s]+\.[^@\s]+$', email))
def is_valid_phone(phone): return phone.isdigit() and len(phone) >= 10
def is_valid_rating(r): return r.isdigit() and 1 <= int(r) <= 5

# ------------------- Main Test Function -------------------

def run_test():
    print("\n🏨 Welcome to Royal Stay Hotel 🏨")

    name = input_validated("Enter guest name: ", is_valid_name, "Name must contain only letters.")
    email = input_validated("Enter guest email: ", is_valid_email, "Invalid email format.")
    phone = input_validated("Enter contact number: ", is_valid_phone, "Phone must be numeric and at least 10 digits.")

    guest = Guest(name, email, phone)

    rooms = [
        Room(101, "Single", ["Wi-Fi", "TV"], 300),
        Room(102, "Double", ["Wi-Fi", "Mini-Bar"], 450),
        Room(201, "Suite", ["Wi-Fi", "Jacuzzi"], 800)
    ]

    print("\n🛏️ Available Rooms:")
    for r in rooms:
        if r.is_available():
            print(r)

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

    while True:
        check_in = input_date("Enter check-in date (YYYY-MM-DD): ")
        check_out = input_date("Enter check-out date (YYYY-MM-DD): ")
        if check_out <= check_in:
            print("❌ Check-out date must be after check-in date.")
        else:
            break

    reservation = Reservation(guest, selected_room, check_in, check_out)
    guest.add_reservation(reservation)
    selected_room.set_availability(False)
    print("\n✅ Reservation Confirmed:", reservation)

    invoice = Invoice(reservation)
    print("\n🧾 Invoice:")
    print(invoice)

    service_type = input_validated("Enter service needed (e.g., Housekeeping): ", lambda s: len(s.strip()) > 0, "Service cannot be empty.")
    service = ServiceRequest(guest, service_type)
    print(service)
    service.mark_completed()
    print("After completion:", service)

    rating_input = input_validated("Rate your stay (1-5): ", is_valid_rating, "Rating must be a number between 1 and 5.")
    comment = input("Leave a comment: ")
    feedback = Feedback(guest, int(rating_input), comment)
    print("\n🗣️ Feedback received:")
    print(feedback)

if __name__ == '__main__':
    run_test()
