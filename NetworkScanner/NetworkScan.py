#! /usr/bin/env python3

import scapy.all as scapy

def scan(ip):
    print(ip)
    scapy.arping(ip)

scan("192.168.0.0/24")