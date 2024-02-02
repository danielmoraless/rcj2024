import RPi.GPIO as GPIO
import lib.core.utils.GeneralUtils as GeneralUtils
import lib.core.actuators.Motors as Motors
import lib.core.sensors.ColorSensor as ColorSensor
import conf

GPIO.setmode(GPIO.BCM)

GeneralUtils.setup_all(conf.pines)

controlador = Motors.L298N(conf.l298n_p, 12500)
controlador.start(0)
sensor_colores = ColorSensor.TCS3200(GPIO, conf.colorSensor1, 10, 0.01)

def loop():
	if sensor_colores.color() == "RED":
		controlador.forward(90)

if __name__ == "__main__":
	try:
		while True:
			loop()
	finally:
		GPIO.cleanup()