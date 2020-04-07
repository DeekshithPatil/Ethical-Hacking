#!/usr/bin/env python

import subprocess
import optparse


def get_arguments():
    parser = optparse.OptionParser()

    parser.add_option("-i", "--interface", dest="interface", help="Interface to change the MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments)=parser.parse_args()

    if not options.interface:
        #code to handle error
        parser.error(" Please specify an interface, use --help for info.")

    elif not options.new_mac:
        #code to handle error
        parser.error(" Please specify an interface, use --help for info.")
    return options



def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " To " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    subprocess.call(["ifconfig", interface])


options = get_arguments()


change_mac(options.interface, options.new_mac)

