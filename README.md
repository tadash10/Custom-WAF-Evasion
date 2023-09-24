# Custom-WAF-Evasion

# Web Application Security Testing Toolkit

A collection of Python scripts for testing web application security, including SQL injection, evasion techniques, and more.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Scripts](#scripts)
  - [advanced_payloads.py](#advanced_payloadspy)
  - [crawler_scanner.py](#crawler_scannerpy)
  - [custom_headers_cookies.py](#custom_headers_cookiespy)
  - [custom_testing.py](#custom_testingpy)
  - [http_methods.py](#http_methodspy)
  - [parameter_discovery.py](#parameter_discoverypy)
  - [proxy_support.py](#proxy_supportpy)
  - [rate_limit_handling.py](#rate_limit_handlingpy)
  - [response_analysis.py](#response_analysispy)
  - [response_time_analysis.py](#response_time_analysispy)
  - [session_handling.py](#session_handlingpy)

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/web-security-toolkit.git

   Navigate to the project directory:cd web-security-toolkit


Install the required Python packages:

pip install -r requirements.txt

Usage
General Usage

    Before using any script, ensure you have completed the installation steps.

    Each script can be run independently by executing it using Python. For example:python advanced_payloads.py

        Follow the specific instructions provided in each script's documentation for customization and usage.

Scripts
advanced_payloads.py

This script generates advanced payloads for web application testing, including SQL injection evasion techniques, encoding, obfuscation, and time-based attacks.
crawler_scanner.py

A web crawler and scanner that automatically discovers and tests multiple pages within a web application. Useful for identifying and exploiting SQL injection vulnerabilities across the application.
custom_headers_cookies.py

Allows users to set custom HTTP headers and cookies when sending requests. Useful for mimicking real-world scenarios and evading Web Application Firewalls (WAFs) that rely on specific headers or cookies.
custom_testing.py

Enables users to define custom testing strategies, including specifying which payloads to test on specific parameters. Provides flexibility in adapting the script to specific web applications.
http_methods.py

Extends the script's capabilities to support various HTTP methods, such as GET, POST, PUT, and DELETE. Offers a broader range of testing capabilities for different web endpoints.
parameter_discovery.py

Automatically discovers input parameters in the target URL and generates payloads for each parameter. Useful for identifying additional injection points in web applications.
proxy_support.py

Allows users to configure proxy settings for requests, enabling routing traffic through different proxies or VPNs for anonymity and bypassing IP-based restrictions.
rate_limit_handling.py

Implements rate-limiting mechanisms to avoid overloading the target server with requests. Ensures that the script remains stealthy and doesn't trigger security alarms.
response_analysis.py

Implements an automated response analysis function that parses and analyzes responses for signs of evasion success. Checks for changes in content, status codes, or response headers that indicate successful evasion.
response_time_analysis.py  .

Analyzes response times to detect time-based SQL injection vulnerabilities. Implements timing attacks to identify delays caused by successful injections.
session_handling.py

Implements session management to maintain session state across multiple requests. Important for testing scenarios where SQL injection requires a valid session.
License

This project is licensed under the MIT License.


