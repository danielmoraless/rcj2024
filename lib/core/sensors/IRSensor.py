import RPi.GPIO as gpio

class IR:
  def __init__(self, pins: tuple) -> None:
    self.pins = pins
  
  def read(self) -> list:
    values = []
    for pin in self.pins:
      values.append(gpio.input(pin))
    
    return values