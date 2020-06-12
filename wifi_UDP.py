import socket 

UDP_IP = "192.168.43.71" 
UDP_PORT = 50000 

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sock.sendto("Hello, this is test",(UDP_IP, UDP_PORT))
