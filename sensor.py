#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
AQ_UID = "GKX" # Change XYZ to the UID of your Air Quality Bricklet
MASTER_UID= "6e7cYn"

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_air_quality import BrickletAirQuality
from tinkerforge.brick_master import BrickMaster

# Callback function for all values callback
def cb_all_values(iaq_index, iaq_index_accuracy, temperature, humidity, air_pressure):
    print("IAQ Index: " + str(iaq_index))


    print("Temperature: " + str(temperature/100.0) + " °C")
    print("Humidity: " + str(humidity/100.0) + " %RH")
    print("Air Pressure: " + str(air_pressure/100.0) + " hPa")
    print("")

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    aq = BrickletAirQuality(AQ_UID, ipcon) # Create device object
    master = BrickMaster(MASTER_UID, ipcon)
    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected
    master.disable_status_led()
    aq.set_status_led_config(0)
    # Register all values callback to function cb_all_values
    aq.register_callback(aq.CALLBACK_ALL_VALUES, cb_all_values)

    # Set period for all values callback to 1s (1000ms)
    aq.set_all_values_callback_configuration(1000, False)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()