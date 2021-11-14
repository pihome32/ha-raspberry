#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "N2q" # Change XYZ to the UID of your Remote Switch Bricklet 2.0

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_remote_switch_v2 import BrickletRemoteSwitchV2

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    rs = BrickletRemoteSwitchV2(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd

    rs.set_remote_configuration(1,15,False)

    rs.switch_socket_b(54266240,0,0)

    ipcon.disconnect()