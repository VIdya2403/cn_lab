routing_table={
    "192.168.1.2":"AA:BB:CC:11:22:33",
    "192.168.1.3":"DD:EE:FF:44:55:66"
}
destination=input("enter ip address")
if destination in routing_table:
    print("mac address found",routing_table[destination])
else:
    print("not found")