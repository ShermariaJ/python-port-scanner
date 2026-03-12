#module helps python programs to communicate over a network
import socket

## Import threading to scan multiple ports at the same time
import threading

#ask the user to enter the ip address they want to scan
target = input("Enter target IP address:")

#define the range of ports that is wanted to scan
start_port = 1
end_port = 1024

#display a message showing which taregt is being scanned
print(f"\nScanning {target}...\n")

# function that scans a single port
def scan_port(port):

    #create a new socket object for each connection attempt
    #AF_INET indicates we are using IPv4 addresses
    #SOCK_STREAM indicates we are using TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #set a timeout so the scanner does not wait too long for a response
    # if a port does not respond within 0.5 seconds, it moves to the next one
    sock.settimeout(0.5)

    #attempt to connect to the target IP and port
    # connect_ex() returns 0 of the connection is successful
    # any other number means the port is closed or unreachable
    result = sock.connect_ex((target, port))

    #if the connection is successful, print the open port
    if result == 0:
        print(f"Port {port}: Open")

    # Close socket
    sock.close()


# create threads to scan ports
for port in range(start_port, end_port + 1):

    thread = threading.Thread(target=scan_port, args=(port,))
    thread.start()

    
