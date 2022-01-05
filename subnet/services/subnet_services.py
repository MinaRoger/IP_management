from ipaddress import IPv4Address

from subnet.models.subnet import MAX_MASK_SIZE


def get_last_subnet_ip(network_ip, mask):
    return str(IPv4Address(str(network_ip)) + (2 ** (MAX_MASK_SIZE - mask)) - 1)
