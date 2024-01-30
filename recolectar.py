import RPi.GPIO as GPIO
import os.path as path
import time
import json

import lib.core.sensors.ColorSensor as ColorSensor
import conf

GPIO.setmode(GPIO.BCM)

def color_sensor_data():
	"""
	Se desean recolectar la lecturas para analizar el comportamiento del sensor.
	Las variables son:
		- Colores: ROJO, VERDE, AZUL, NEGRO, BLANCO.
		- Número de ciclos: [10, 20, 30, 40, 50]
		- Delay de cada lectura: [0.01, 0.1]
	"""
	json_data = {}

	for color in ("ROJO", "VERDE", "AZUL", "NEGRO", "BLANCO"):
		input(f"¿Color {color} listo?")
		json_data[color] = {}

		for ciclos in range(10, 60, 10):
		json_data[color][ciclos] = {}

			for delay in (0.01, 0.1):
				sensor = ColorSensor.TCS3200(GPIO, conf.colorSensor1, ciclos, delay)

				rgb_time_start = time.time()
				lectura_rgb = sensor.get_rgb()
				rgb_time_end = time.time()
				lectura_color = sensor.color()
				color_time_end = time.time()

				json_data[color][ciclos][delay] = {
					"get_rgb": {
						"valor": lectura_rgb,
						"tiempo": rgb_time_end-rgb_time_start,
					},
					"color": {
						"valor": lectura_color,
						"tiempo": color_time_end-rgb_time_end,
					},
				}

	with open(path.join("rdata", "color_sensor_data.json"), "w") as data_file:
		data_file.write(json.dumps(json_data))