from lib.core.sensors.ColorSensor import TCS3200
from lib.core.sensors.IRSensor import IR
from lib.core.actuators.Motors import L298N

class Follower:
  def __init__(self, tcs1: TCS3200, tcs2: TCS3200, l298n: L298N, ir: IR) -> None:
    self.tcs1 = tcs1
    self.tcs2 = tcs2
    self.l298n = l298n
    self.ir = ir
    self.last_ir_state = None
  
  def calculate_direction_by_ir(self):
    (l, r) = self.last_ir_state = self.ir.read()

    if r and l: # ambos están en blanco
      return "F" # forward - avanza
    elif not r and l: # el derecho está en negro y el izquierdo en blanco
      return "R" # right - giro a la derecha
    elif not l and r: # el izquierdo está en negro y el derecho en blanco
      return "L" # left - giro a la izquierda
    elif not r and not l: # ambos en negro
      return "B" # B de backward o de both, como quieras. El punto es que ambos están en negro
  
  def calculate_direction_by_color(self) -> str:
    left_color = self.tcs1.color()
    right_color = self.tcs2.color()

    if left_color and right_color == "WHITE":
      return "F" # forward
    elif left_color == "BLACK" and right_color == "WHITE":
      return "L" # left
    elif right_color == "BLACK" and left_color == "WHITE":
      return "R" # right
    elif left_color and right_color == "BLACK":
      return "B" # backward o both
    elif left_color and right_color == "GREEN":
      return "180T" # giro de 180 grados
    elif left_color == "GREEN":
      return "90LT" # giro de 90 grados a la izquierda
    elif right_color == "GREEN":
      return "90RT" # giro de 90 grados a la derecha
  
  def react_by_color(self):
    direction = self.calculate_direction_by_color()

    if direction == "F" or direction == "B":
      self.l298n.forward(100)
    elif direction == "L":
      self.l298n.rotar_izquierda(100)
    elif direction == "R":
      self.l298n.rotar_derecha(100)
    
    #TODO: crear métodos para giros graduales y añadirlos aquí