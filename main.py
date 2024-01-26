import RPi.GPIO as GPIO
import lib.core.sensors.ColorSensor as ColorSensor
import lib.core.utils.GeneralUtils as GeneralUtils

GPIO.setmode(GPIO.BCM)

cs1_p = {
	"S2": 17,
	"S3": 27,
	"OUT": 22,
}

pines = {
	"IN": {
		"OUT": 22,
	},
	"OUT": {
		"S2": 17,
		"S3": 27,
	},
}

COLORES = {
	"ROJO": [0, 0],
	"AZUL": [0, 1],
	"VERDE": [1, 1],
	"SF": [1, 0],
}

def setup():
	GPIO.setup(cs1_p["OUT"], GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GeneralUtils.setup_all(pines)

def loop():
	sensor_de_color_1 = ColorSensor.TCS3200(GPIO, cs1_p)
	while True:
		rojo = sensor_de_color_1.read_once(COLORES["ROJO"], 10, 0.3)
		azul = sensor_de_color_1.read_once(COLORES["AZUL"], 10, 0.3)
		verde = sensor_de_color_1.read_once(COLORES["VERDE"], 10, 0.3)
		print(f"R: {rojo}\nG: {verde}\nB: {azul}\n\n")

if __name__ == "__main__":
	setup()
	try:
		loop()
	finally:
		GPIO.cleanup()