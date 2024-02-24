import time
import RPi.GPIO as gpio

class TCS3200:
	"""
	La clase TCS3200 proporciona las funciones necesarias
	para utilizar el sensor de color TCS3200 de forma
	sencilla.

		Parámetros:
			ref (dict): Valores de referencia para cada color.
			pins (dict): Un diccionario con los nombres y número de cada pin.
			ncycles (int): Número de ciclos para calcular la salida del sensor.
			delay (float): Tiempo de espera para equilibrar el sensor entre
						   cada lectura.
	"""
	def __init__(self, ref: dict, pins: dict, ncycles: int, delay: float, debug: bool = False):
		super(TCS3200, self).__init__()
		self.ref = ref
		self.pins = pins
		self.ncycles = ncycles
		self.delay = delay
		self.debug = debug

	def read_once(self, color: tuple) -> float:
		"""
		TCS3200.read_once configura los pines (S2, S3)
		y calcula la salida del sensor, una sola vez.

			Parámetros:
				color (tuple): Configuración para los pines [S2, S3] respectivamente.

			Retorna:
				La lectura en Hz con la configuración asignada. (float)
		"""
		time.sleep(self.delay)
		gpio.output(self.pins["S2"], color[0])
		gpio.output(self.pins["S3"], color[1])
		timerStart = time.time()
		for _ in range(self.ncycles):
			gpio.wait_for_edge(self.pins["OUT"], gpio.FALLING)
		return (self.ncycles/(time.time()-timerStart))

	def get_rgb(self) -> tuple:
		"""
		get_rgb hace una lectura para cada configuración de color (rojo, azul, verde).

			Retorna:
				Una tuple con el valor de cada lectura en el orden RGB. (tuple)
		"""
		rgb = (self.read_once((0, 0)), self.read_once((1, 1)), self.read_once((0, 1)))

		return rgb

	def color(self):
		rgb = self.get_rgb()
		suma = sum(rgb)

		for colorName in self.ref:
			if suma >= self.ref[colorName]["min"] and suma <= self.ref[colorName]["max"]:
				if self.debug:
					print(f"DEBUG (TCS3200.color): {(colorName, rgb)}")

				return colorName
