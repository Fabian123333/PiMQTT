#!/usr/bin/env python

import config as conf
import paho.mqtt.client as mqtt
import time
import json
import traceback

from modules import configParser as configParser

from sensors import bodenfeuchtigkeit as bodenfeuchtigkeit
from sensors import am2302 as am2302
from actors import switch as switch

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
	device = msg.topic.replace(config.mqtt["topic"] + "/", "")
	print(str(msg.topic)+" "+str(msg.payload))
	
	try:
		toggleActor(device, msg.payload)
	except Exception as error:
		print(traceback.format_exc())

def toggleActor(device, msg):
	data = json.loads(msg)
	type = config.actors[device]["type"]
	if "action" in data:
		if(type == "switch"):
			if(data["action"] == "on"):
				print "setOn switch " + device
				switch.setOn(config.actors[device]["gpio"])
				client.publish(config.mqtt["topic"] + "/" + device, json.dumps({"state": "setOn"}))
			elif(data["action"] == "off"):
				print "setOff switch " + device
				switch.setOff(config.actors[device]["gpio"])
				client.publish(config.mqtt["topic"] + "/" + device, json.dumps({"state": "setOff"}))
			
			

def setupMQTT():
	client = mqtt.Client()

	# Setup MQTT Client ID

	client.reinitialise(client_id=config.mqtt["client-id"], clean_session=True, userdata=None)
	
	client.on_connect = on_connect
	client.on_message = on_message
	
	client.connect(config.mqtt["host"], config.mqtt["port"], config.mqtt["keepalive"])
	client.loop_start()
	client.subscribe(config.mqtt["topic"] + "/stellung")
	return client

def getSensor(sensor):
	if(sensor["type"] == "bodenfeuchtigkeit"):
		return bodenfeuchtigkeit.getValue(sensor["channel"])
	if(sensor["type"] == "temperature"):
		return am2302.getTemperature(sensor["gpio"])
	if(sensor["type"] == "humidity"):
		return am2302.getHumidity(sensor["gpio"])				

def getActor(actor):
	if(actor["type"] == "switch"):
		switch.setOn(actor["gpio"])
		return switch.getStatus(actor["gpio"])

def initActors(client):
	for actor in config.actors:
		#print "init " + actor + " as " + config.actors[actor]["type"]
		try:
			if(config.actors[actor]["type"] == "switch"):
				switch.__init__(config.actors[actor]["gpio"])
				client.subscribe(config.mqtt["topic"] + "/" + actor)
		except Exception as error:
			print(traceback.format_exc())
		

def __main__():
	initActors(client)

	while True:
		payload = {
			"STATE": "1"
		}
	
		for sensor in config.sensors:
			try:
				payload[sensor] = getSensor(config.sensors[sensor])
			except Exception as error:
				print(traceback.format_exc())
		
		for actor in config.actors:
			try:
				payload[actor] = getActor(config.actors[actor])
			except Exception as error:
				print(traceback.format_exc())
		
		print(payload)
		
		client.publish(config.mqtt["topic"] + "/general", json.dumps(payload))
		time.sleep(config.interval)

config = configParser.run(conf)
client = setupMQTT()
__main__()