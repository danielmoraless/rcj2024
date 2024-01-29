import RPi.GPIO as GPIO
import lib.core.sensors.ColorSensor as ColorSensor
import lib.core.utils.GeneralUtils as GeneralUtils
from conf import pines

GPIO.setmode(GPIO.BCM)

cs1_p = {
	"S2": 17,
	"S3": 27,
	"OUT": 22,
}

def setup():
	GPIO.setup(cs1_p["OUT"], GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GeneralUtils.setup_all(pines)

def loop():
	sensor_de_color_1 = ColorSensor.TCS3200(GPIO, cs1_p, 10, 0.1)
	while True:
		rgb = sensor_de_color_1.get_rgb()
		color = sensor_de_color_1.color(False)
		print(f"\n---\nRESULTADOS DE LECTURA:\n\t* RGB: {rgb}\n\t* COLOR:{color}\n---")

if __name__ == "__main__":
	setup()
	try:
		loop()
	finally:
		GPIO.cleanup()