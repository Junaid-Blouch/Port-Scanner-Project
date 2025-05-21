# ---------------------------
# Port Scanner Project
# Developed by: Muhammad Junaid
# University: MNS UET Multan
# Subject: Information Security Lab
# ---------------------------

import socket

# Set the target IP address (localhost)
target = "127.0.0.1"  # You can change this to scan another IP

# Function to check if a specific port is open
def portScanner(port):
    try:
        # Create a new socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Try to connect to the target port
        sock.connect((target, port))
        
        # Close the socket after checking
        sock.close()
        return True
    except:
        return False

# Loop through port numbers from 1 to 1024
for port in range(1, 1025):  # 1025 included for complete scan
    result = portScanner(port)

    if result:
        print(f"Port {port} is OPEN!")
    else:
        print(f"Port {port} is CLOSED!")

# Optional: Test for a specific port
print("Testing custom port (8080):", portScanner(8080))
