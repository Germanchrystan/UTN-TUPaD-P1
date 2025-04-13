import math

def es_radio_valido(intInput: str) -> bool:
  try:
    rad = float(intInput)
    return rad > 0
  except ValueError:
    return False

def obtener_radio() -> float:
  intInput = 0
  while True:
    intInput = input(f"Ingrese el radio: ")
    if es_radio_valido(intInput):
      return float(intInput)
    else:
      print("radio no válido")

def calcular_perimetro_circulo(radius: float) -> float:
  return round(math.pi * 2 * radius, 2)

def calcular_area_circulo(radius: float) -> float:
  return round(math.pi * radius ** 2, 2)

radius = obtener_radio()
perimeter = calcular_perimetro_circulo(radius)
area = calcular_area_circulo(radius)
print(f"El perímetro del círculo es: {perimeter}. Su área es {area}")