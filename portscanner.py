# Port Scanner - Information Security Lab Project 01
# Created by Muhammad Junaid

import socket

target = input("Enter the IP address to scan: ")
print("Scanning target:", target)

for port in range(1, 1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.5)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} is open")
    s.close()
