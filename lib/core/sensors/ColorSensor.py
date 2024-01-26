import time

class TCS3200:
	"""
	La clase TCS3200 proporciona las funciones necesarias
	para utilizar el sensor de color TCS3200 de forma
	sencilla.

		Parámetros:
			gpio (RPi.GPIO): GPIO de Raspberrypi 4.
			pins (dict): Un diccionario con los nombres y número de cada pin.
	"""
	def __init__(self, gpio, pins):
		super(TCS3200, self).__init__()
		self.gpio = gpio
		self.pins = pins

	def read_once(self, color: list, ncycles: int, delay: float) -> float:
		"""
		TCS3200.read_once configura los pines (S2, S3)
		y calcula la salida del sensor, una sola vez.

			Parámetros:
				color (list): Configuración para los pines [S2, S3] respectivamente.
				ncycles (int): Número de ciclos para calcular la salida del sensor.
				delay (float): Tiempo de espera para equilibrar el sensor entre cada
							   lectura.

			Retorna:
				La lectura en Hz con la configuración asignada. (float)
		"""
		time.sleep(delay)
		self.gpio.output(self.pins["S2"], color[0])
		self.gpio.output(self.pins["S3"], color[1])
		timerStart = time.time()
		for _ in range(ncycles):
			self.gpio.wait_for_edge(self.pins["OUT"], self.gpio.FALLING)
		return (ncycles/(time.time()-timerStart))

	def get_rgb(ncycles: int, delay: float) -> list:
		r = read_once([0, 0], ncycles, delay)
		g = read_once([1, 1], ncycles, delay)
		b = read_once([0, 1], ncycles, delay)
		return [r, g, b]

	def color(ncycles: int, delay: float):
		rgb = self.get_rgb(ncycles, delay)
		sum = rgb[0]+rgb[1]+rgb[2]

		if rgb[0] > rgb[1] and rgb[0] > rgb[2]:
			return "RED"
		elif rgb[1] > rgb[0] and rgb[1] > rgb[2]:
			return "GREEN"
		elif rgb[2] > rgb[0] and rgb[2] > rgb[1]:
			return "BLUE"
		elif sum >= 3000:
			return "WHITE"
		elif sum <= 600:
			return "BLACK"