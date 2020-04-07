#This program is used to print the sniffed packet
#Note that here we are not man in the middle and we are just printing any our packet (Packets that pass through eth0 interface)
#Open browser after running the code to check output

import scapy.all as scapy

def sniff(interface):
    scapy.sniff(iface= interface, store = False, prn = process_sniffed_packet)


def process_sniffed_packet(packet):
    print(packet)

sniff("eth0")