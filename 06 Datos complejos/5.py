import math

class Circulo:
  def __init__(self, radio):
    self.radio = radio

  def calcular_area(self):
    return round(math.pi * self.radio ** 2, 2)
  def calcular_perimetro(self):
    return round(math.pi * 2 * self.radio, 2)