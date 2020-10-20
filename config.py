interval = 60

mqtt = {
	"host": "10.100.2.10",
	"port": 1883,
	"topic": "default/monitor",
	"client-id": "default-monitor",
	"keepalive": 60
}

spi = {
	"CLK"  : 11,
	"MISO" : 9,
	"MOSI" : 10,
	"CS"   : 8
}

sensors = {
#	"SOIL_MOISTURE_1": {
#		"type": "bodenfeuchtigkeit",
#		"channel": 0
#	},
#       "SOIL_MOISTURE_2": {
#               "type": "bodenfeuchtigkeit",
#               "channel": 1
#       },
#        "SOIL_MOISTURE_3": {
#                "type": "bodenfeuchtigkeit",
#                "channel": 2
#        },
#	"ZULUFT_TEMPERATUR": {
#               "type": "temperature",
#               "gpio": 22
#	},
#        "ZULUFT_HUMIDITY": {
#               "type": "humidity",
#               "gpio": 22
#        },
#	"ZELT_TEMPERATUR": {
#		"type": "temperature",
#		"gpio": 24
#	},
#	"ZELT_HUMIDITY": {
#		"type": "humidity",
#		"gpio": 24
#	},
#	"FRISCHLUFT_TEMPERATUR": {
#		"type": "temperature",
#		"gpio": 17
#	},
#	"FRISCHLUFT_HUMIDITY": {
#		"type": "humidity",
#		"gpio": 17
#	},
#	"RAUMLUFT_TEMPERATUR": {
#		"type": "temperature",
#		"gpio": 27
#	},
#	"RAUMLUFT_HUMIDITY": {
#		"type": "humidity",
#		"gpio": 27
#	}
}

actors = {
	"PUMPE_{1-4}": {
		"type": "switch",
		"default": "off",
		"gpio": {17, 27, 22, 23}
	}
}
