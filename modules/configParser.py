import re

def run(config):
	newActors = {}
	newSensors = {}
	
	for actor in config.actors:
		print "parse actor " + actor
		r = re.search("(.*)(\{([0-9]+)\-([0-9]+)\})", actor)
		if r:
			print "optimize config for " + r.group(0) + " (" + r.group(1) + "," + r.group(2) + "," + r.group(3) + "," + r.group(4) + ")"
			
			gpio = list(config.actors[actor]["gpio"])
			n = 0
			
			for i in range(int(r.group(3)), int(r.group(4)) + 1):
				newActor = config.actors[actor]
				
				newName = r.group(1) + str(i)
				newActors[newName] = {}
				newActors[newName]["type"] = config.actors[actor]["type"]
				newActors[newName]["default"] = config.actors[actor]["default"]
				newActors[newName]["gpio"] = int(gpio[n]) 
				
				n = n + 1

		else:
			print "migrate actor " + actor
			newActors[actor] = config.actors[actor]

	print newActors
	config.actors = newActors

	for sensor in config.sensors:
		print "parse sensor " + sensor
		r = re.search("(.*)(\{([0-9]+)\-([0-9]+)\})", sensor)
		if r:
			print "optimize config for " + r.group(0) + " (" + r.group(1) + "," + r.group(2) + "," + r.group(3) + "," + r.group(4) + ")"
			
			gpio = list(config.sensors[sensor]["gpio"])
			n = 0
			
			for i in range(int(r.group(3)), int(r.group(4)) + 1):
				newSensor = config.sensors[sensor]
				
				newName = r.group(1) + str(i)
				newSensors[newName] = {}
				newSensors[newName]["type"] = config.sensors[sensor]["type"]
				newSensors[newName]["default"] = config.sensors[sensor]["default"]
				newSensors[newName]["gpio"] = int(gpio[n]) 
				
				n = n + 1

		else:
			print "migrate sensor " + sensor
			newSensors[sensor] = config.sensors[sensor]

	print newSensors
	config.sensors = newSensors


	return config