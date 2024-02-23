import RPi.GPIO as GPIO
import os
from lib.core.sensors.ColorSensor import TCS3200
from lib.core.utils.GeneralUtils import setup_all
import conf

GPIO.setmode(GPIO.BCM)
setup_all(conf.pines)

sensor = TCS3200(GPIO, conf.colorSensor1, 10, 0.1)

ciclos = int(input("[?] Número de ciclos de calibración: "))
nlecturas = int(input("[?] Número de lecturas en cada ciclo: "))
resultados = {}

while True:
	input("[...] Presione Enter para comenzar")
	color = str(input("[?] Escriba el color a calibrar: "))
	print(f"[+] Leyendo para {color}...")

	min_list = []
	max_list = []

	for i in range(ciclos):
		lecturas = []

		for j in range(nlecturas):
			lecturas.append(sum(sensor.get_rgb()))

		lecturas = lecturas[1:] # generalmente, la primera lectura es incoherente. Omitimos
		min_list.append(min(lecturas))
		max_list.append(max(lecturas))

	minimo_promedio = sum(min_list)/ciclos
	maximo_promedio = sum(max_list)/ciclos
	resultados[color] = {
		"min": minimo_promedio,
		"max": maximo_promedio,
	}

	print(f"[+] {nlecturas*ciclos} lecturas realizadas para \"{color}\":")
	print(f"\t[INFO] Mínimo: {minimo_promedio}")
	print(f"\t[INFO] Máximo: {maximo_promedio}")

	if input("[?] ¿Desea continuar? (y/n): ") == "n":
		break

data_dir = "florence_data"
os.makedirs(data_dir, exist_ok=True)

with open(os.path.join(data_dir, "calibrate.json"), "w") as data_file:
	data_file.write(json.dumps(resultados))

print(f"[+] ¡Datos guardados en {os.getcwd()}/{data_dir}/calibrate.json!")
