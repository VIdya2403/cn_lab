import socket 
import json


def checksum(wordds):
    total = 0

    for w in words:
        total+= int(w,2)

    while total > 255:
        total = (total&255) + (total >> 8)

    return (~total)&255


n = int(input("enter no of data words : "))

words = []

for i in range(n):
    words.append(input("enter data word:"))

check = checksum(words)

print("original data words:",words)
print("checksum : ",format(check,"08b"))

print("1) no error\n2)single bit error\n3)multi bit error\n")
ch = input("enter choice[1-3] : ")

send_words = words.copy()

if ch == "2" : 

    x = list(send_words[0])
    x[0] = "1" if x[0] == "0" else "0"
    send_words[0] = "".join(x)

if ch == "3":
    x = list(send_words[0])
    x[0] = "1" if x[0] == "0" else "0"
    send_words[0] = "".join(x)

    x = list(send_words[1])
    x[0] = "1" if x[0] == "0" else "0"
    send_words[1] = "".join(x)


print("transmitted words : ",send_words)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("192.168.1.8",6000))

data = {
    "words": words,
    "checksum":format(check,"08b")
}

client.sendall(json.dumps(data).encode())


reply = json.loads(client.recv(1024).decode())

print("result : ",reply["status"])

print("message : ",reply["message"])

client.close()