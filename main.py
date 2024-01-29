import RPi.GPIO as GPIO
import lib.core.sensors.ColorSensor as ColorSensor
import lib.core.utils.GeneralUtils as GeneralUtils
import conf

GPIO.setmode(GPIO.BCM)

def setup():
	GPIO.setup(conf.colorSensor1["OUT"], GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GeneralUtils.setup_all(conf.pines)

def loop():
	sensor_de_color_1 = ColorSensor.TCS3200(GPIO, conf.colorSensor1, 10, 0.1)
	while True:
		rgb = sensor_de_color_1.get_rgb()
		color = sensor_de_color_1.color()
		print(f"\n---\nRESULTADOS DE LECTURA:\n\t* RGB: {rgb}\n\t* COLOR:{color}\n---")

if __name__ == "__main__":
	setup()
	try:
		loop()
	finally:
		GPIO.cleanup()