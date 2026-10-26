import socket

client = socket.socket()
client.connect(("192.168.1.8",6001))

domain = input("enter domain name:")

client.send(domain.encode())

ip = client.recv(1024).decode()

print("IP address:",ip)
client.close()

