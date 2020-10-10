# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import config as config

# Software SPI configuration:
#CLK  = 23
#MISO = 21
#MOSI = 19
#CS   = 24



def getConnection():
	return Adafruit_MCP3008.MCP3008(clk=config.spi["CLK"], cs=config.spi["CS"], miso=config.spi["MISO"], mosi=config.spi["MOSI"])
