#!/usr/bin/env python
# -*- coding: utf-8 -*-
from paho.mqtt import client as mqtt_client
import time
import json

mqtt_broker="10.70.1.95"
mqtt_port=1883
mqtt_client_id="tinkerforge_living"


HOST = "localhost"
PORT = 4223
AQ_UID = "GKX" # Change XYZ to the UID of your Air Quality Bricklet
MASTER_UID = "6e7cYn"

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_air_quality import BrickletAirQuality
from tinkerforge.brick_master import BrickMaster


def connect_mqtt():
	def on_connect(client, userdata, flags, rc):
		if rc == 0:
			print("Connected to MQTT Broker!")
		else:
			print("Failed to connect, return code %d\n", rc)
    # Set Connecting Client ID
	client = mqtt_client.Client(mqtt_client_id)
	client.username_pw_set("mqtt", "cairnsD18")
	client.on_connect = on_connect
	client.connect(mqtt_broker, mqtt_port)
	return client

def publish(client,topic,msg):
	msg_count = 0
	while True:
		time.sleep(1)
		result = client.publish(topic, msg,retain=True)
        # result: [0, 1]
		status = result[0]

		msg_count += 1
# Callback function for all values callback
def cb_all_values(iaq_index, iaq_index_accuracy, temperature, humidity, air_pressure):


	data = {'temp': temp, 'humidity': humidity/100.0, 'iaq_index':iaq_index,'iaq_index_accuracy':iaq_index_accuracy}
	data_out=json.dumps(data)
	
	publish(client,"ha/sensor/living_room/air_quality/state",data_out)
	
if __name__ == "__main__":
	ipcon = IPConnection() # Create IP connection
	 # Create device object
	master = BrickMaster(MASTER_UID, ipcon)
	ipcon.connect(HOST, PORT) 
	master.disable_status_led()# Connect to brickd
    # Don't use device before ipcon is connected
	ipcon.disconnect()
	time.sleep(1)
	ipcon = IPConnection()
	aq = BrickletAirQuality(AQ_UID, ipcon)
	
	ipcon.connect(HOST, PORT)
	aq.set_status_led_config(0)
	aq.set_temperature_offset(150)
	
	client = connect_mqtt()
	client.loop_start()
	publish(client,"ha/sensor/living_room/air_quality/available","online")
    # Register all values callback to function cb_all_values
	aq.register_callback(aq.CALLBACK_ALL_VALUES, cb_all_values)

    # Set period for all values callback to 1s (1000ms)
	aq.set_all_values_callback_configuration(1000, False)

	input("Press key to exit\n") # Use raw_input() in Python 2
	ipcon.disconnect()
