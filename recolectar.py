import RPi.GPIO as GPIO
import os.path as path
import time
import json
import os
import argparse

import lib.core.sensors.ColorSensor as ColorSensor
import lib.core.utils.GeneralUtils as GeneralUtils
import conf

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--type", dest="type", default="calibrate", help="Tipo de recolección de datos")

args = parser.parse_args()

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
		# setup
		GeneralUtils.setup_all(conf.pines)

		# "loop"
		input(f"¿Color {color} listo?")
		json_data[color] = {}

		for ciclos in range(10, 60, 10):
			json_data[color][ciclos] = {}
			print(f"[+] Entrando con {ciclos} ciclos...")

			for delay in (0.01, 0.1):
				json_data[color][ciclos][delay] = {}
				print(f"\t[+] Entrando con {delay} segundos...")

				for lectura in range(0, 31):
					print(f"\t\t[+] Ejecutando lectura #{lectura}...")
					sensor = ColorSensor.TCS3200(GPIO, conf.colorSensor1, ciclos, delay)

					rgb_time_start = time.time()
					lectura_rgb = sensor.get_rgb()
					rgb_time_end = time.time()
					lectura_color = sensor.color()
					color_time_end = time.time()

					json_data[color][ciclos][delay][lectura] = {
						"get_rgb": {
							"valor": lectura_rgb,
							"tiempo": rgb_time_end-rgb_time_start,
						},
						"color": {
							"valor": lectura_color,
							"tiempo": color_time_end-rgb_time_end,
						},
					}

	print("[+] Guardando...")
	d = "rdata"
	os.makedirs(d, exist_ok=True)

	with open(path.join(d, "color_sensor_data.json"), "w") as data_file:
		data_file.write(json.dumps(json_data))

def calibrate_data():
	input("Presione Enter para iniciar")
	GeneralUtils.setup_all(conf.pines)
	sensor = ColorSensor.TCS3200(GPIO, conf.colorSensor1, 10, 0.01)
	resultados = {}

	while True:
		lecturas = []
		print("[+] Realizando lecturas...")
		time_start = time.time()
		for _ in range(97):
			lecturas.append(sum(sensor.get_rgb()))
		time_end = time.time()
		
		print(f"[+] 97 lecturas realizadas en {time_end-time_start} segundos")
		color = str(input("[?] Indique el color leido: "))
		resultados[color] = {
			"min": min(lecturas),
			"max": max(lecturas),
		}
		if input("[?] Desea culminar? (y/n): ") == "n":
			break
	
	print("[+] Guardado resultados...")
	d = "rdata"
	os.makedirs(d, exist_ok=True)

	with open(path.join(d, "calibrate_data.json"), "w") as data_file:
		data_file.write(json.dumps(resultados))
	
	print("[+] ¡Datos de calibración recolectados!")

try:
	match args.type:
		case "all":
			color_sensor_data()
		case "calibrate":
			calibrate_data()
		case _:
			print("Tipo de recolección no reconocido.")
finally:
	GPIO.cleanup()