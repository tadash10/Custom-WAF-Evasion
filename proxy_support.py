# proxy_support.py

import requests

class ProxyHandler:
    def __init__(self, proxy_url):
        self.proxy_url = proxy_url
        self.session = requests.Session()
        self.session.proxies = {"http": self.proxy_url, "https": self.proxy_url}

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
    proxy_handler = ProxyHandler("http://your-proxy-url.com")
    
    # Make a sample request
    response = proxy_handler.get("https://example.com")
    
    print(response.text)
    
    proxy_handler.close()
