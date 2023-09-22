# http_methods.py

import requests

class HTTPMethodTester:
    def __init__(self, target_url):
        self.target_url = target_url

    def send_request(self, method, headers=None, params=None):
        try:
            if method == "GET":
                response = requests.get(self.target_url, headers=headers, params=params)
            elif method == "POST":
                response = requests.post(self.target_url, headers=headers, data=params)
            elif method == "PUT":
                response = requests.put(self.target_url, headers=headers, data=params)
            elif method == "DELETE":
                response = requests.delete(self.target_url, headers=headers, params=params)
            else:
                raise ValueError("Unsupported HTTP method")
            
            return response

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None

# Example usage:
if __name__ == "__main__":
    target_url = "https://example.com/vulnerable_endpoint"
    tester = HTTPMethodTester(target_url)
    
    # Send a GET request
    response = tester.send_request("GET")
    print(response.text)
    
    # Send a POST request with custom headers and parameters
    headers = {"Content-Type": "application/json"}
    params = {"param1": "value1", "param2": "value2"}
    response = tester.send_request("POST", headers=headers, params=params)
    print(response.text)
