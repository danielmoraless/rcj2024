import RPi.GPIO as gpio

class IR:
  def __init__(self, pinl: int, pinr: int) -> None:
    self.pinl = pinl
    self.pinr = pinr
  
  def read(self) -> tuple:
    return (gpio.input(self.pinl), gpio.input(self.pinr))