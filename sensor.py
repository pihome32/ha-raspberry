
#!/usr/bin/python3

# -*- coding: utf-8 -*-
from paho.mqtt import client as mqtt_client
import time
import json
import logging as log
log.basicConfig(level=log.INFO)


from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_air_quality import BrickletAirQuality
from tinkerforge.brick_master import BrickMaster


class bbTinkerforge:
	mqtt_broker="10.70.1.95"
	mqtt_port=1883
	mqtt_client_id="tinkerforge_living"


	HOST = "localhost"
	PORT = 4223
	AQ_UID = "GKX" # Change XYZ to the UID of your Air Quality Bricklet
	MASTER_UID = "6e7cYn"
	ipcon = None
	
	def __init__(self):

		self.ipcon = IPConnection()
		while True:
			try:
				self.ipcon.connect(bbTinkerforge.HOST, bbTinkerforge.PORT)
				break
			except Error as e:
				log.error('Connection Error: ' + str(e.description))
				time.sleep(1)
			except socket.error as e:
				log.error('Socket error: ' + str(e))
				time.sleep(1)
		self.ipcon.register_callback(IPConnection.CALLBACK_ENUMERATE, self.cb_enumerate)
		self.ipcon.register_callback(IPConnection.CALLBACK_CONNECTED, self.cb_connected)

		while True:
			try:
				self.ipcon.enumerate()
				break
			except Error as e:
				print(e.description)
				log.error('Enumerate Error: ' + str(e.description))
				time.sleep(1)

	def cb_air_quality(self, iaq_index, iaq_index_accuracy, temperature, humidity, air_pressure):
		if self.aq is not None:
			print(iaq_index)
			data = {'temperature': temperature/100.0, 'humidity': humidity/100.0, 'iaq_index':iaq_index,'iaq_index_accuracy':iaq_index_accuracy}
			data_out=json.dumps(data)
			#client=mqtt_client.Client(mqtt_client_id)
			#client.username_pw_set("mqtt", "cairnsD18")
			#client.connect(mqtt_broker, mqtt_port)
			
			#client.publish("ha/sensor/living_room/air_quality/state",data_out)
			#client.disconnect


	def cb_enumerate(self, uid, connected_uid, position, hardware_version,firmware_version, device_identifier, enumeration_type):
		if enumeration_type == IPConnection.ENUMERATION_TYPE_CONNECTED or enumeration_type == IPConnection.ENUMERATION_TYPE_AVAILABLE:
			print("wenu")
			if device_identifier == BrickletAirQuality.DEVICE_IDENTIFIER:
				try:
					self.aq = BrickletAirQuality(uid, self.ipcon)
					self.aq.set_status_led_config(0)
					self.aq.set_temperature_offset(150)
					self.aq.register_callback(self.aq.CALLBACK_ALL_VALUES, self.cb_air_quality)
					self.aq.set_all_values_callback_configuration(1000, False)
					log.info('Air quality initialised')
				except Error as e:
					log.error('Air quality init failed: ' + str(e.description))
					self.aq = None

	def cb_connected(self, connected_reason):
		if connected_reason == IPConnection.CONNECT_REASON_AUTO_RECONNECT:
			log.info('Auto Reconnect')

			while True:
				try:
					self.ipcon.enumerate()
					break
				except Error as e:
					log.error('Enumerate Error: ' + str(e.description))
					time.sleep(1)


	#ipcon.disconnect()
if __name__ == "__main__":
	bb_tinkerforge = bbTinkerforge()
	if bb_tinkerforge.ipcon != None:
		bb_tinkerforge.ipcon.disconnect()
	
