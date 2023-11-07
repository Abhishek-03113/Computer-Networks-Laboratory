import ipaddress

ip=input("Enter IP address: ")

subnet=ipaddress.IPv4Network(f"{ip}/24",strict=False)

ipclass=subnet.network_address.packed[0]//32

print(subnet.netmask)
print(ipclass)