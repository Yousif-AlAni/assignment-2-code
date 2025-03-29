class Invoice:
    """Generates an invoice for a reservation."""

    def __init__(self, reservation, charges=50, discount=20):
        # Initialize invoice with charges and discounts
        self.__reservation = reservation  # Reservation to bill
        self.__charges = charges          # Extra charges
        self.__discount = discount        # Discount applied

    def calculate_total(self):
        # Calculate total cost: nights * rate + charges - discount
        nights = (self.__reservation.get_check_out() - self.__reservation.get_check_in()).days
        return nights * self.__reservation.get_room().get_price_per_night() + self.__charges - self.__discount

    def __str__(self):
        # Return invoice summary
        return f"Invoice for {self.__reservation.get_guest().get_name()}: AED{self.calculate_total()}"
