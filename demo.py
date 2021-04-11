from gpiozero import LED
from time import sleep


white = LED(2)
blue = LED(22)
red = LED(25)
green = LED(15)

def dim(led,brightness,period):
	assert(abs(brightness<1))
	assert(brightness*period<1 and brightness*period>0)
	while True:
		try:
			led.on()
			sleep(brightness*period)
			led.off()
			sleep(period*(1-brightness))
		except KeyboardInterrupt:
			break

if __name__ == '__main__':
	while True:
		for led in [white,blue,red,green]:
			sleep(.05)
			led.on()
			sleep(.1)
			led.off()
			sleep(.05)

