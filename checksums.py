import socket 
import json
import threading


def checksum(words):
    total = 0

    for w in words:
        total+= int(w,2)

    while total > 255:
        total = (total&255) + (total >> 8)

    return (~total)&255


def handle_client(conn):

    data = conn.recv(1024).decode()
    data = json.loads(data)

    words = data["words"]
    check = data["checksum"]

    total = checksum(words+[check])

    if total == 0:
        result = "valid"
        message = "transaction successful"

    else:
        result = "invalid"
        message = "transaction failed :  error"


    print("status : ",result)
    print("message : ",message)

    conn.sendall(json.dumps({
        "status":result,
        "message":message
    }).encode())
    conn.close()


server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind(("192.168.1.8",6000))
server.listen(5)

while True :

    conn,addr = server.accept()
    thread = threading.Thread(
        target = handle_client,
        args = (conn,)
    )
    thread.start()
    break

