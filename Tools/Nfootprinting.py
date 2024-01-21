import socket
from scapy.all import traceroute

def scan_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            s.connect((host, port))
            banner = s.recv(1024).decode('utf-8')
            return True, banner
    except (socket.timeout, ConnectionRefusedError):
        return False, None

def traceroute_analysis(target):
    tracert_result, _ = traceroute(target, maxttl=20)
    return tracert_result

def validate_target(input_target):
    try:
        socket.inet_pton(socket.AF_INET, input_target)
        return True
    except socket.error:
        try:
            socket.gethostbyname(input_target)
            return True
        except socket.error:
            return False

def main():
    while True:
        target = input("Enter a website name or IP address: ")
        while not validate_target(target):
            print("\nInvalid input. Please enter a valid IP address or domain name.")
            target = input("\nEnter a website name or IP address: ")

        common_ports = [21, 22, 25, 53, 80, 110, 143, 443, 445, 3389, 3306, 5432, 123]

        for port in common_ports:
            port_status, banner = scan_port(target, port)
            if port_status:
                print(f"Port {port} is open. Banner: {banner}")
            else:
                print(f"Port {port} is closed.")

        tracert_result = traceroute_analysis(target)
        print("\nTraceroute Analysis:")
        for hop in tracert_result:
            print(f"{hop[1].src} ({hop[0].dst})")

        another_scan = input("\nDo you want to scan another target? (yes/no): ")
        if another_scan.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
