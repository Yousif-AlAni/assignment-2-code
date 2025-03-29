from datetime import datetime
import re
from room import Room
from guest import Guest
from reservation import Reservation
from invoice import Invoice
from payment import Payment
from service import ServiceRequest
from feedback import Feedback

# ---------------------- Input Validations ----------------------

def input_validated(prompt, condition_fn, error_msg):
    """Prompt input until valid."""
    while True:
        value = input(prompt)
        if condition_fn(value):
            return value
        print("❌", error_msg)

def input_date(prompt):
    """Validate date input."""
    while True:
        try:
            return datetime.strptime(input(prompt), "%Y-%m-%d").date()
        except ValueError:
            print("❌ Invalid date format. Please use YYYY-MM-DD.")

# ---------------------- Validation Helpers ----------------------

def is_valid_name(name): return name.replace(" ", "").isalpha()
def is_valid_email(email): return bool(re.match(r'^[^@\s]+@[^@\s]+\.[^@\s]+$', email))
def is_valid_phone(phone): return phone.isdigit() and len(phone) >= 10
def is_valid_rating(r): return r.isdigit() and 1 <= int(r) <= 5

# ---------------------- Main Program ----------------------

def main():
    print("\n🏨 Welcome to Royal Stay Hotel 🏨")

    # Guest creation with input validation
    name = input_validated("Enter guest name: ", is_valid_name, "Name must contain only letters.")
    email = input_validated("Enter guest email: ", is_valid_email, "Invalid email format.")
    phone = input_validated("Enter contact number: ", is_valid_phone, "Phone must be at least 10 digits.")
    guest = Guest(name, email, phone)

    # Room list (predefined)
    rooms = [
        Room(101, "Single", ["Wi-Fi", "TV"], 300),
        Room(102, "Double", ["Wi-Fi", "Mini-Bar"], 450),
        Room(201, "Suite", ["Wi-Fi", "Jacuzzi"], 800)
    ]

    print("\n🛏️ Available Rooms:")
    for room in rooms:
        if room.is_available():
            print(room)

    # Room selection
    while True:
        room_input = input("Enter room number to book: ").strip()
        if not room_input.isdigit():
            print("❌ Please enter a valid numeric room number.")
            continue
        room_number = int(room_input)
        selected_room = next((r for r in rooms if r.get_room_number() == room_number and r.is_available()), None)
        if selected_room:
            break
        print("❌ Selected room is not available or does not exist.")

    # Date selection
    while True:
        check_in = input_date("Enter check-in date (YYYY-MM-DD): ")
        check_out = input_date("Enter check-out date (YYYY-MM-DD): ")
        if check_out <= check_in:
            print("❌ Check-out must be after check-in.")
        else:
            break

    # Create reservation
    reservation = Reservation(guest, selected_room, check_in, check_out)
    guest.add_reservation(reservation)
    selected_room.set_availability(False)
    print("\n✅ Reservation Confirmed:")
    print(reservation)

    # Invoice
    invoice = Invoice(reservation)
    print("\n🧾 Invoice:")
    print(invoice)

    # Payment
    method = input_validated("Enter payment method (Credit Card / Wallet): ",
                             lambda s: s.strip() != "", "Payment method cannot be empty.")
    payment = Payment(method)
    payment.process_payment(invoice.calculate_total())

    # Service request
    service_type = input_validated("Enter service needed (e.g., Housekeeping): ",
                                   lambda s: len(s.strip()) > 0, "Service cannot be empty.")
    service = ServiceRequest(guest, service_type)
    print(service)
    service.mark_completed()
    print("After completion:", service)

    # Feedback
    rating_input = input_validated("Rate your stay (1-5): ", is_valid_rating, "Rating must be between 1 and 5.")
    comment = input("Leave a comment: ")
    feedback = Feedback(guest, int(rating_input), comment)
    print("\n🗣️ Feedback received:")
    print(feedback)

    # Loyalty points summary
    print(f"\n⭐ Loyalty Points Earned: {guest.get_loyalty_points()}")

# Run the program
if __name__ == '__main__':
    main()
