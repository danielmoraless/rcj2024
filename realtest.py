import argparse

import RPi.GPIO as GPIO
import lib.core.sensors.ColorSensor as ColorSensor
import lib.core.utils.GeneralUtils as GeneralUtils
import conf

# Configuración para RPi

GPIO.setmode(GPIO.BCM)

# Configuración para este script

parser = argparse.ArgumentParser()

parser.add_argument("-t", "--test", dest="testname", default="colorsensor-1", help="Nombre de la prueba")

args = parser.parse_args()

# colorsensor-1

def csu_setup():
	GPIO.setup(conf.colorSensor1["OUT"], GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GeneralUtils.setup_all(conf.pines)

def csu_loop():
	sensor_de_color_1 = ColorSensor.TCS3200(GPIO, conf.colorSensor1, 10, 0.1)
	while True:
		rgb = sensor_de_color_1.get_rgb()
		color = sensor_de_color_1.color()
		print(f"\n---\nRESULTADOS DE LECTURA:\n\t* RGB: {rgb}\n\t* COLOR:{color}\n---")

def colosensor_1():
	try:
		csu_setup()
		csu_loop()
	finally:
		GPIO.cleanup()


# script

match args.testname:
	case "colorsensor-1":
		colosensor_1()
	case _:
		print(f"No existen pruebas con el nombre {args.testname}")