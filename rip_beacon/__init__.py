#!/usr/bin/python

import struct
import socket
import sys
import time
import argparse

RIP_ADDRESS = "224.0.0.9"
RIP_PORT = 520


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interval", type=int, default=30)
    parser.add_argument("routes", nargs="+")
    args = parser.parse_args()

    data = struct.pack("!BBHHH", 2, 2, 0, socket.AF_INET, 0)
    for route in args.routes:
        address, _, cidr = route.partition("/")
        cidr = int(cidr)
        if cidr < 1 or cidr > 32:
            raise ValueError("Invalid CIDR: %s" % route)
        data += struct.pack(
            "!4sLLL", socket.inet_aton(address), ((2 ** cidr) - 1) << (32 - cidr), 0, 1
        )

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("", RIP_PORT))
    while True:
        sock.sendto(data, (RIP_ADDRESS, RIP_PORT))
        time.sleep(args.interval)


if __name__ == "__main__":
    main()
