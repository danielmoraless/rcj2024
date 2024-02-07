import RPi.GPIO as GPIO
import lib.core.utils.GeneralUtils as GeneralUtils
import lib.core.actuators.Motors as Motors
import lib.core.sensors.ColorSensor as ColorSensor
import conf
import time

GPIO.setmode(GPIO.BCM)

GeneralUtils.setup_all(conf.pines)

controlador = Motors.L298N(conf.l298n_p, 12500)
controlador.start(0)
sensor_colores = ColorSensor.TCS3200(GPIO, conf.colorSensor1, 10, 0.1)

def loop():
	time.sleep(2)
	color = sensor_colores.color()
	print(color)
	if color == "WHITE":
		controlador.forward(90)
	if color == "RED":
		controlador.backward(90)

if __name__ == "__main__":
	try:
		while True:
			loop()
	finally:
		GPIO.cleanup()