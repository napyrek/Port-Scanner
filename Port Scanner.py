import socket # importing socket module

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # using internet socket, using TCP
s.settimeout(5) # set timeout to improve scan speed

host = input('Enter the IP you would like to scan: ') # getting IP from user
port = int(input('Enter the port you would like to scan: ')) # getting port from user

def portScanner(port):
    if s.connect((host, port)): # using target ip and ports to be scanned
        print(f'Port {port} is closed on {host}')
    else:
        print(f'Port {port} is open on {host}')

portScanner(port)



