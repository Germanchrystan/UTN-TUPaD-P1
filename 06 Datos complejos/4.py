class Persona:
  def __init__(self, nombre, pais, edad):
    self.nombre = nombre
    self.pais = pais
    self.edad = edad
  
  def saludar(self):
    print(f"¡Hola! Soy {self.nombre}, vivo en {self.pais} y tengo {self.edad} años.")

persona = Persona("Germán", "Argentina", 34)
persona.saludar()