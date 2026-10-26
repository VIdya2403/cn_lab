import socket 

server = socket.socket()
server.bind(("192.168.1.8",6001))
server.listen(1)
print("root server running...")

while True:
    conn,addr = server.accept()
    domain = conn.recv(1024).decode()

    c = socket.socket()
    c.connect(("192.168.1.8",6002))
    print("domain name sent to tld")
    c.send(domain.encode())
    result = c.recv(1024).decode()
    c.close()


    conn.send(result.encode())
    conn.close()

