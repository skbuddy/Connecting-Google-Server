#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 13:36:16 2020

@author: skbuddy
"""


import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

local_hostname = socket.gethostbyname("www.google.com")

local_fqdn = socket.getfqdn()

#ip_address = socket.gethostbyname(local_hostname)

server_address = (local_hostname, 80)

s.connect(server_address)

print("Connecting to Google Server %s (%s) %s" % (local_hostname, local_fqdn, ip_address))

print("Successfully Connected to the Google")

s.close()
