#This program allows us to obtain the MAC address of the devices in a separate variable

#! /usr/bin/env python3

import scapy.all as scapy


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered= scapy.srp(arp_request_broadcast, timeout=1)[0] #receive only the first among the returned lists as only answered list is important

    for element in answered:
        print(element[1].psrc)
        print(element[1].hwsrca)
        print("----------------------------------------")


scan('10.0.2.1/24')
