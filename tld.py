import socket 
server = socket.socket()
server.bind(("192.168.1.8",6002))
server.listen(1)
print("tld server running...")

while True:
    conn,addr = server.accept()
    domain = conn.recv(1024).decode()

    if "." in domain:
        print("domain name valid")
        c = socket.socket()
        c.connect(("192.168.1.8",6003))
        c.send(domain.encode())
        result = c.recv(1024).decode()
        c.close()
    else:
        print("domain name not valid")
        break

    conn.send(result.encode())
    conn.close()