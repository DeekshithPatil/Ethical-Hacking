#This code is used to convert NetfilterQueue ppackets to scapy

#!/usr/bin/env python3import netfilterqueue

import netfilterqueue
import scapy.all as scapy
import time

def process_packet(packet):
    scapy_packet=scapy.IP(packet.get_payload())
    try:
        if scapy_packet[scapy.DNS]:
            print(scapy_packet.show())
    except:
        time.sleep(0.5)

    packet.accept()


queue = netfilterqueue.NetfilterQueue()
queue.bind(1, process_packet)
queue.run()


