import RPi.GPIO as GPIO
import lib.core.utils.GeneralUtils as GeneralUtils
import lib.core.actuators.Motors as Motors
import lib.core.sensors.ColorSensor as ColorSensor
import conf
import json
import os

GPIO.setmode(GPIO.BCM)

GeneralUtils.setup_all(conf.pines)

controlador = Motors.L298N(conf.l298n_p, 12500)
controlador.start(0)

sensor_colores = ColorSensor.TCS3200(conf.colorSensor1, 10, 0.1, debug=True)

def loop():
	color = sensor_colores.color()
	match color:
		case "WHITE":
			controlador.forward(95)
		case "BLACK":
			controlador.rotar_izquierda(95)
		case "RED":
			controlador.backward(95)
		case "BLUE":
			controlador.rotar_derecha(95)
		case _:
			print(f"color {color} no reconocido")

if __name__ == "__main__":
	try:
		while True:
			loop()
	except KeyboardInterrupt:
		exit(0)
	finally:
		GPIO.cleanup()
