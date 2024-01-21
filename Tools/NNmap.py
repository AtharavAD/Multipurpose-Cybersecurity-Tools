import nmap
import re

ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
port_min = 0
port_max = 65535

open_ports = []
ip_address = None  # Initialize ip_address to None

while True:
    if ip_address is None:
        while True:
            ip_add_entered = input("\nPlease enter the IP address that you want to scan: ")
            if ip_add_pattern.search(ip_add_entered):
                ip_address = ip_add_entered  # Store the entered IP address
                print(f"\n{ip_address} is a valid IP address")
                break

    print("\nOptions:")
    print("1. Host Discovery")
    print("2. Port Scanning with Defined Range")
    print("3. Service Version Detection for Specified Port")
    print("4. OS Detection for Specified Port")
    print("5. UDP Scanning")
    print("6. Firewall Evasion Techniques")
    print("7. Stealth Scanning")
    print("8. Exit\n")

    option = input("Select an option (1-8): ")

    if option == '1':
        # Host discovery
        nm = nmap.PortScanner()
        nm.scan(ip_address, arguments='-sn')  # '-sn' option for host discovery

        # Check if any hosts were discovered
        if nm.all_hosts():
            for host in nm.all_hosts():
                print(f"\nHost {host} is up")
        else:
            print("\nNo hosts are up.")


    elif option == '2':
        while True:
            print("Please enter the range of ports you want to scan in format: <int>-<int> (e.g., 60-120)")
            port_range = input("Enter port range: ")
            port_range_valid = port_range_pattern.search(port_range.replace(" ", ""))
            if port_range_valid:
                port_min = int(port_range_valid.group(1))
                port_max = int(port_range_valid.group(2))
                break

        # Port scanning
        nm = nmap.PortScanner()
        nm.scan(ip_address, f'{port_min}-{port_max}')
        for port in range(port_min, port_max + 1):
            try:
                port_status = nm[ip_address]['tcp'][port]['state']
                print(f"Port {port} is {port_status}")
            except KeyError:
                print(f"Cannot get information for port {port}.")

    elif option == '3':
        # Service version detection
        port_to_scan = input("Enter the port for service version detection: ")
        nm = nmap.PortScanner()
        nm.scan(ip_address, arguments=f'-p {port_to_scan} -sV')
        try:
            service = nm[ip_address]['tcp'][int(port_to_scan)]['name']
            version = nm[ip_address]['tcp'][int(port_to_scan)]['version']
            print(f"Service on port {port_to_scan} is {service} (Version: {version})")
        except KeyError:
            print(f"Cannot get information for port {port_to_scan}.")

    elif option == '4':
        # OS detection
        port_to_scan = input("Enter the port for OS detection: ")
        nm = nmap.PortScanner()
        nm.scan(ip_address, arguments=f'-p {port_to_scan} -O')

        if 'osmatch' in nm[ip_address] and nm[ip_address]['osmatch']:
            os_guess = nm[ip_address]['osmatch'][0]['osclass'][0]['osfamily']
            print(f"OS guess for host {ip_address} on port {port_to_scan}: {os_guess}")
        else:
            print(f"No OS information available for host {ip_address} on port {port_to_scan}.")

    elif option == '5':
        # UDP scanning
        nm = nmap.PortScanner()
        nm.scan(ip_address, arguments='-sU')
        for port in nm[ip_address].all_udp():
            state = nm[ip_address]['udp'][port]['state']
            print(f"UDP Port {port} is {state}")

    elif option == '6':
        # Firewall evasion techniques (example options, adjust as needed)
        evasion_options = input("Enter Nmap evasion options (e.g., -f, -D RND:10): ")
        nm = nmap.PortScanner()
        nm.scan(ip_address, arguments=f'{evasion_options}')
        for port in nm[ip_address].all_protocols():
            port_info = nm[ip_address][port]
            for p in port_info:
                print(f"Port {p} is {port_info[p]['state']}")

    elif option == '7':
        # Stealth scanning options (example options, adjust as needed)
        stealth_options = input("Enter Nmap stealth scanning options (e.g., -sS, -sT): ")
        nm = nmap.PortScanner()
        nm.scan(ip_address, arguments=f'{stealth_options}')
        for port in nm[ip_address].all_protocols():
            port_info = nm[ip_address][port]
            for p in port_info:
                print(f"Port {p} is {port_info[p]['state']}")

    elif option == '8':
        exit(0)  # Exit the program

    else:
        print("Invalid option. Please select 1, 2, 3, 4, 5, 6, 7, or 8.")
