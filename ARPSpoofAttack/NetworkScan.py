#This program is the improved version of FinalNetScan.py which makes use of dictionaries

#! /usr/bin/env python3

import scapy.all as scapy


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered= scapy.srp(arp_request_broadcast, timeout=1, verbose= False)[0]
    clients_list = []
    for element in answered:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list


def print_result(results_list):
    print("IP\t\t\tMAC\n---------------------------")
    for client in results_list:
        print(client["ip"]+"\t\t"+client["mac"])


scan_result = scan('10.0.2.1/24')
print_result(scan_result)
