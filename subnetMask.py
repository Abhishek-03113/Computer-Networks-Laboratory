def calculate_subnet_mask(ip, prefix_length):
    if prefix_length < 0 or prefix_length > 32:
        return "Invalid prefix length"

    # Initialize the subnet mask as a list of 32 zeros
    subnet_mask = [0] * 32

    # Set the first 'prefix_length' bits to 1 in the subnet mask
    for i in range(prefix_length):
        subnet_mask[i] = 1

    # Convert the list of bits to a string
    subnet_mask_str = ".".join(
        [
            str(int("".join(map(str, subnet_mask[i : i + 8])), 2))
            for i in range(0, 32, 8)
        ]
    )

    return subnet_mask_str


# Test cases
test_cases = [
    ("192.168.1.10", 24),  # Test case 1: Subnet mask for 192.168.1.10/24
    ("10.0.0.5", 16),  # Test case 2: Subnet mask for 10.0.0.5/16
    ("172.16.0.1", 20),  # Test case 3: Subnet mask for 172.16.0.1/20
]

for ip, prefix_length in test_cases:
    subnet_mask = calculate_subnet_mask(ip, prefix_length)
    print(
        f"IP: {ip}, Subnet Prefix Length: {prefix_length}, Subnet Mask: {subnet_mask}"
    )
