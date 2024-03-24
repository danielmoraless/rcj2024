import RPi.GPIO as GPIO
import lib.core.utils.GeneralUtils as GeneralUtils
from lib.core.sensors.ColorSensor import TCS3200
from lib.core.sensors.IRSensor import IR
from lib.core.actuators.Motors import L298N
from lib.LineFollower import Follower
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

	global sensor_color1
	global sensor_color2
	global ir
	global motores
	global seguidor

	sensor_color1 = TCS3200(conf.colorSensor1)
	sensor_color2 = TCS3200(conf.colorSensor2)
	ir = IR(conf.IR_1, conf.IR_2)
	motores = L298N(conf.l298n_p, 15000)
	seguidor = Follower(sensor_color1, sensor_color2, motores, ir)

def loop():
	seguidor.calculate_direction_by_color()

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
