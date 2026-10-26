bit1 = 1
bit2 = 0

if bit1 == 0:
    bit1 = -1

if bit2 == 0:
    bit2 = -1
code1 = [1,1,-1,-1]
code2 = [1,-1,1,-1]

received = []

signal1 = [bit1 * x for x in code1]
signal2 = [bit2 * x for x in code2]

for i in range(4):
    received.append(signal1[i]+signal2[i])

total1 = 0

for i in range(4):
    total1 += received[i]*code1[i]

result1 = total1/4

if result1 > 0:
    decoded1 = 1
else:
    decoded1 = 0

total2 = 0

for i in range(4):
    total2+= received[i]*code2[i]

result2 = total2/4

if result2 >0:
    decoded2 = 1
else:
    decoded2 = 0

print("decoded data 1 :",decoded1)
print("decoded data 2 :",decoded2)


