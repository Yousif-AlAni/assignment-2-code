class Payment:
    """Handles payment processing."""

    def __init__(self, method):
        # Initialize payment method (e.g. Credit Card, Wallet)
        self.__method = method

    def process_payment(self, amount):
        # Simulate payment processing
        print(f"✅ Payment of AED{amount} processed via {self.__method}.")
