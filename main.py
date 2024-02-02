import RPi.GPIO as GPIO
import lib.core.utils.GeneralUtils as GeneralUtils
import lib.core.actuators.Motors as Motors
import conf

GPIO.setmode(GPIO.BCM)

GeneralUtils.setup_all(conf.pines)

controlador = Motors.L298N(conf.l298n_p, 12500)
controlador.start(0)

def loop():
	velocidad = int(input("Ingrese la velocidad: "))
	controlador.forward(velocidad)
	if input("¿Desea seguir? ") == "n":
		controlador.stop()
		GPIO.cleanup()
		os.exit(0)

if __name__ == "__main__":
	try:
		while True:
			loop()
	finally:
		GPIO.cleanup()