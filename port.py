#!/bin/python3

import socket
import pyfiglet

# Display a banner
print(pyfiglet.figlet_format("Port_EX"))

def scan_ports(target):
    print(f"\nScanning {target} for open ports...\n")
    
    open_ports = []
    for port in range(1, 65536):  # Scanning all 65,535 ports
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)  # Set timeout to avoid long waits
        
        result = s.connect_ex((target, port))  # Connect to port
        if result == 0:  # If port is open
            try:
                service = socket.getservbyport(port)  # Get service name
            except:
                service = "Unknown Service"
            open_ports.append((port, service))
            print(f"[+] Port {port} is open ({service})")
        
        s.close()
    
    if not open_ports:
        print("[-] No open ports found.")

    return open_ports

# Get user input
target_ip = input("Enter target IP address: ")
scan_ports(target_ip)
