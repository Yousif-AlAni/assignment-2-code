class ServiceRequest:
    """Tracks a service request from a guest."""

    def __init__(self, guest, service_type):
        # Initialize service request
        self._guest = guest
        self.__service_type = service_type  # e.g., Housekeeping
        self.__status = "Pending"           # Default status

    def mark_completed(self):
        # Mark the request as completed
        self.__status = "Completed"

    def __str__(self):
        # Return request summary
        return f"Service Request: {self.__service_type} for {self._guest.get_name()} - Status: {self.__status}"
