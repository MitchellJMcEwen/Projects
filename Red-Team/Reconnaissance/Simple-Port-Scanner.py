#!/bin/python3


import sys
import socket
from datetime import datetime

# Define the target

# Check number of arguments given = 2
def check_args():
    if len(sys.argv) != 2:
        print("Invalid number of arguments.")
        print("Syntax: python3 scanner.py {IP ADDRESS}")
        sys.exit(1)

# Check for valid IP address
def valid_ip(s):
    # Validate number of "."
    ip_list = s.split('.')
    if len(ip_list) != 4:
        return False

    # Check range of each number in the IP address
    for element in ip_list:
        if not element.isdigit() or int(element) < 0 or int(element) > 255 or (element[0] == '0' and len(element) != 1):
            return False
    return True

check_args()

if valid_ip(sys.argv[1]):
    # Translate hostname to IPv4 if known by DNS
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid IP address.")
    print("IP Address Syntax: X.X.X.X")
    sys.exit(1)

# Banner
print("-" * 50)
print("Scanning target: " + target)
print("Time started: " + str(datetime.now()))
print("-" * 50)


try:
	for port in range(1,1000):
		# Gather IPv4 and port
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		# IP supplied by argv 1
		result = s.connect_ex((target,port))
		# Open port = 0, closed port =1
		if result == 0:
			print(f"Port {port} is open")
		s.close()

except KeyboardInterrupt:
	print("\nExiting program.")
	sys.exit()
	
except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()

except socket.error:
	print("Could not connect to server.")
	sys.exit()

