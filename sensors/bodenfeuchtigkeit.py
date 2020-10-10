import time
import spi_con as spi

mcp = spi.getConnection()

def getValue(channel):
	val = mcp.read_adc(channel)
	val = 1024 - val
	return val