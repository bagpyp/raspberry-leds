from gpiozero import LEDBoard
from time import sleep, time

leds = LEDBoard(2,22,25,15)

def dim(led, brightness, duration=1, period=.001):
	assert(abs(brightness<1))
	t = time()
	while time() < t+duration:
		try:
			led.on()
			sleep(brightness*period)
			led.off()
			sleep(period*(1-brightness))
		except KeyboardInterrupt:
			break
		

if __name__ == '__main__':
	while True:
		try:
			for led in leds:
				sleep(.05)
				led.on()
				sleep(.1)
				led.off()
				sleep(.05)
		except KeyboardInterrupt:
			break

	for led in leds:
		for i in range(1,10):
			dim(led, i/10, duration=.1)

