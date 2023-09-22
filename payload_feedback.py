# payload_feedback.py

class PayloadFeedbackLoop:
    def __init__(self):
        self.successful_payloads = []
        self.failed_payloads = []

    def add_successful_payload(self, payload):
        self.successful_payloads.append(payload)

    def add_failed_payload(self, payload):
        self.failed_payloads.append(payload)

    def get_feedback_summary(self):
        summary = {
            "successful_payloads": self.successful_payloads,
            "failed_payloads": self.failed_payloads
        }
        return summary

# Example usage:
if __name__ == "__main__":
    feedback_loop = PayloadFeedbackLoop()
    
    # Provide feedback for successful and failed payloads
    feedback_loop.add_successful_payload("payload1")
    feedback_loop.add_failed_payload("payload2")
    
    # Get feedback summary
    summary = feedback_loop.get_feedback_summary()
    print("Successful Payloads:", summary["successful_payloads"])
    print("Failed Payloads:", summary["failed_payloads"])
