import RPi.GPIO as GPIO
import lib.core.utils.GeneralUtils as GeneralUtils
import conf

trigger = False

def update_trigger():
	global trigger
	if GPIO.input(conf.BUTTON):
		if trigger:
			trigger = False
		else:
			trigger = True

def setup():
	GPIO.setmode(GPIO.BCM)
	GeneralUtils.setup_all(conf.pines)
	GPIO.setup(conf.BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def loop():
	# codigo principal
	pass

if __name__ == "__main__":
	try:
		setup()
		while True:
			update_trigger()
			if trigger: loop()
	except KeyboardInterrupt:
		pass
	finally:
		GPIO.cleanup()
