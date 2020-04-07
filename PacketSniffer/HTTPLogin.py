#This code is used to print the Login details of websites that use HTTP

# This program prints only the HTTP packets
# Before running the code, run: pip install scapy_http

import scapy.all as scapy
from scapy.layers import http


def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)


def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        print(packet.show())


sniff("eth0")
