#!/bin/python3

import os

print("You are using a BASIC NMAP SCAN...")

ip = input("Enter an IP ")

os.system("sudo nmap -A -sT  -O -T4 -Pn -oN basic_nmap_scan.txt " + ip)
