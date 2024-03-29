import RPi.GPIO as gpio

class L298N:
  def __init__(self, pines, frecuencia):
    self.pines = pines
    self.frecuencia = frecuencia
    self.pwma = gpio.PWM(self.pines["ENA"], self.frecuencia)
    self.pwmb = gpio.PWM(self.pines["ENB"], self.frecuencia)
  
  def start(self, dc_start):
    self.pwma.start(dc_start)
    self.pwmb.start(dc_start)
  
  def stop_pwm(self):
    self.pwma.stop()
    self.pwmb.stop()
  
  def cambiar_estado_izquierdo(self, estado: tuple, vel: float):
    gpio.output(self.pines["IN1"], estado[0])
    gpio.output(self.pines["IN2"], estado[1])
    self.pwma.ChangeDutyCycle(vel)
  
  def cambiar_estado_derecho(self, estado: tuple, vel: float):
    gpio.output(self.pines["IN3"], estado[0])
    gpio.output(self.pines["IN4"], estado[1])
    self.pwmb.ChangeDutyCycle(vel)
  
  def forward(self, vel: float):
    self.cambiar_estado_izquierdo((0, 1), vel)
    self.cambiar_estado_derecho((0, 1), vel)
  
  def backward(self, vel: float):
    self.cambiar_estado_izquierdo((1, 0), vel)
    self.cambiar_estado_derecho((1, 0), vel)
  
  def rotar_izquierda(self, vel: float):
    self.cambiar_estado_derecho((0, 1), vel)
    self.cambiar_estado_izquierdo((1, 0), vel)

  def rotar_derecha(self, vel):
    self.cambiar_estado_izquierdo((0, 1), vel)
    self.cambiar_estado_derecho((1, 0), vel)
  
  def stop(self):
    self.pwma.ChangeDutyCycle(0)
    self.pwmb.ChangeDutyCycle(0)