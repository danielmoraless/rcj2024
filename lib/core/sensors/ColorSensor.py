import time
import RPi.GPIO as gpio

class TCS3200:
	"""
	La clase TCS3200 proporciona las funciones necesarias
	para utilizar el sensor de color TCS3200 de forma
	sencilla.

		Parámetros:
			gpio (RPi.GPIO): GPIO de Raspberrypi 4.
			pins (dict): Un diccionario con los nombres y número de cada pin.
			ncycles (int): Número de ciclos para calcular la salida del sensor.
			delay (float): Tiempo de espera para equilibrar el sensor entre
						   cada lectura.
	"""
	def __init__(self, pins: dict, ncycles: int, delay: float, debug: bool = False):
		super(TCS3200, self).__init__()
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
		"""
		color obtiene los valores de get_rgb y devuelve el color de con mayor valor.

			Parámetros:
				make_new_read (bool): True si la última lectura está desactualizada
									  y/o no desea utilizarse. False en caso contrario.

			Retorna:
				El nombre del color en inglés y mayúsculas cerradas.
				Colores posibles: RED, GREEN, BLUE, WHITE, BLACK. (str)
		"""
		detected_color = None
		rgb = self.get_rgb()

		sum = rgb[0]+rgb[1]+rgb[2]

		# Los condicionales tienen prioridad de reacción. Es decir,
		# primero se verifican los colores más presentes y que
		# requieran de una rápida reacción.
		# El orden es: WHITE, BLACK, GREEN, RED, BLUE
		if sum >= 3000:
			# Para que sum sea >= 3000, cada valor de RGB debe ser >= 1000
			detected_color = "WHITE"
		elif sum <= 900:
			# Para que sum sea <= 900, cada valor de RGB debe ser <= 300
			detected_color = "BLACK"
		elif rgb[1] > rgb[0] and rgb[1] > rgb[2]:
			detected_color = "GREEN"
		elif rgb[0] > rgb[1] and rgb[0] > rgb[2]:
			detected_color = "RED"
		elif rgb[2] > rgb[0] and rgb[2] > rgb[1]:
			detected_color = "BLUE"

		if self.debug:
			print(f"DEBUG (TCS3200.color): {(detected_color, rgb)}")
		
		return detected_color
