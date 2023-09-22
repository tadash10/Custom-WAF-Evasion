# parameter_discovery.py

from urllib.parse import urlparse, parse_qs

def discover_parameters(target_url):
    parsed_url = urlparse(target_url)
    query_parameters = parse_qs(parsed_url.query)
    return list(query_parameters.keys())

# Example usage:
if __name__ == "__main__":
    target_url = "https://example.com/vulnerable_page.php?param1=value1&param2=value2"
    parameters = discover_parameters(target_url)
    print("Discovered parameters:", parameters)
