# rate_limit_handling.py

import time

class RateLimiter:
    def __init__(self, rate_limit_per_second):
        self.rate_limit = rate_limit_per_second
        self.last_request_time = 0

    def wait(self):
        current_time = time.time()
        time_elapsed = current_time - self.last_request_time
        if time_elapsed < 1 / self.rate_limit:
            time.sleep(1 / self.rate_limit - time_elapsed)
        self.last_request_time = time.time()

# Example usage:
if __name__ == "__main__":
    rate_limiter = RateLimiter(5)  # 5 requests per second
    
    for _ in range(10):
        rate_limiter.wait()
        # Make a sample request here
