import RPi.GPIO as gpio

class IR:
  def __init__(self, pinr: int, pinl: int) -> None:
    self.pinr = pinr
    self.pinl = pinl
  
  def read(self) -> tuple:
    return (gpio.input(self.pinr), gpio.input(self.pinl))