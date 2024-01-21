import threading
import requests

def http_stress_test(target):
    try:
        response = requests.get(target)
        print(f"Request sent to {target}. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def main():
    print("""
    Simple HTTP Stress Tester
    -------------------------
    Enter a target URL to stress test.
    This script will send HTTP GET requests to the target URL using multiple threads.
    Ensure that you have legal authorization before testing on any website or server.
    """)

    target_url = input("Enter the target URL (including http/https): ")

    try:
        threads = int(input("Enter the number of threads: "))
    except ValueError:
        exit("Threads count is incorrect!")

    if threads <= 0:
        exit("Threads count should be greater than 0!")

    for i in range(threads):
        thread = threading.Thread(target=http_stress_test, args=(target_url,))
        thread.start()
        print(f"Thread {i + 1} started!")

if __name__ == "__main__":
    main()
