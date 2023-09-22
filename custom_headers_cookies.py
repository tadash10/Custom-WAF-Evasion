# custom_headers_cookies.py

import requests

class CustomHeadersCookiesTester:
    def __init__(self, target_url):
        self.target_url = target_url

    def send_request(self, method, headers=None, params=None, cookies=None):
        try:
            if method == "GET":
                response = requests.get(self.target_url, headers=headers, params=params, cookies=cookies)
            elif method == "POST":
                response = requests.post(self.target_url, headers=headers, data=params, cookies=cookies)
            else:
                raise ValueError("Unsupported HTTP method")
            
            return response

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None

# Example usage:
if __name__ == "__main__":
    target_url = "https://example.com/vulnerable_endpoint"
    tester = CustomHeadersCookiesTester(target_url)
    
    # Send a GET request with custom headers and cookies
    headers = {"User-Agent": "Custom User Agent"}
    cookies = {"session_id": "12345"}
    response = tester.send_request("GET", headers=headers, cookies=cookies)
    print(response.text)
