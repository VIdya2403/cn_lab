import socket 

server = socket.socket()
server.bind(("192.168.1.8",6003))
server.listen(1)
print("auth server running...")

records = {
    "www.google.com" : "92.168.1.8",
    "www.pinterest.com":"92.168.1.8"
}
while True:
    conn,addr = server.accept()
    domain = conn.recv(1024).decode()

    if domain in records:
        ip = records[domain]
        conn.send(ip.encode())

    else:
        conn.send("ip not found".encode())

    conn.close()