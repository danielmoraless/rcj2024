import RPi.GPIO as GPIO
import lib.core.utils.GeneralUtils as GeneralUtils
import lib.core.actuators.Motors as Motors
import lib.core.sensors.ColorSensor as ColorSensor
import conf
import keyboard

GPIO.setmode(GPIO.BCM)

GeneralUtils.setup_all(conf.pines)

controlador = Motors.L298N(conf.l298n_p, 12500)
controlador.start(0)
sensor_colores = ColorSensor.TCS3200(GPIO, conf.colorSensor1, 10, 0.1)

def loop():
	color = sensor_colores.color()
	if color == "WHITE":
		controlador.forward(90)
	if color == "RED":
		controlador.backward(90)

if __name__ == "__main__":
	try:
		keyboard.add_hotkey('s', lambda: exit(0))
		while True:
			loop()
	except KeyboardInterrupt:
		exit(0)
	finally:
		GPIO.cleanup()