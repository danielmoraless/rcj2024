import RPi.GPIO as GPIO

def setup_all(pins_info: dict):
	"""
	setup_all configura todos los pines especificados
	en entrada y salida, respectivamente

		Parámetros:
			pins_info (dict): Diccionario con los pines de entrada y salida por separado.
	"""
	for inpin in pins_info["IN"].values():
		GPIO.setup(inpin, GPIO.IN)

	for outpin in pins_info["OUT"].values():
		GPIO.setup(outpin, GPIO.OUT)