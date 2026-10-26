import socket

client = socket.socket()
client.connect(("192.168.1.8",6000))

print("client 2 running...")

bit = input("enter user 2 bit (0 or 1): ")

client.sendall(bit.encode())

client.close()