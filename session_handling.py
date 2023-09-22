# session_handling.py

import requests

class SessionHandler:
    def __init__(self):
        self.session = requests.Session()

    def get(self, url, headers=None, params=None):
        if headers:
            response = self.session.get(url, headers=headers, params=params)
        else:
            response = self.session.get(url, params=params)
        return response

    # Add more HTTP methods and functionality as needed

    def close(self):
        self.session.close()

# Example usage:
if __name__ == "__main__":
    session_handler = SessionHandler()
    
    # Make a sample request
    response = session_handler.get("https://example.com")
    
    print(response.text)
    
    session_handler.close()
