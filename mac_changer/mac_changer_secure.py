#!/usr/bin/env python

import subprocess

interface=input("Interface: ")
new_mac=input("MAC Address: ")
print("[+] Changing MAC address for "+interface+" To "+new_mac)

subprocess.call(["ifconfig",interface,"down"])
subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
subprocess.call(["ifconfig",interface,"up"])
subprocess.call(["ifconfig",interface])