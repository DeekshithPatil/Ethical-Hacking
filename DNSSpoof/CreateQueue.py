#This code is to implement a Net Filter Queue using python3

#!/usr/bin/env python3import netfilterqueue

import netfilterqueue

def process_packet(packet):
    print(packet)
    packet.accept()


queue = netfilterqueue.NetfilterQueue()
queue.bind(1, process_packet)
queue.run()


