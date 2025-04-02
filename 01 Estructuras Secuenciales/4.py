import math

def isValidRadius(intInput: str) -> bool:
  try:
    rad = float(intInput)
    return rad > 0
  except ValueError:
    return False

def getRadius() -> float:
  intInput = 0
  while True:
    intInput = input(f"Ingrese el radio: ")
    if isValidRadius(intInput):
      return float(intInput)
    else:
      print("radio no válido")

def getPerimeter(radius: float) -> float:
  return round(math.pi * 2 * radius, 2)

def getArea(radius: float) -> float:
  return round(math.pi * radius ** 2, 2)

radius = getRadius()
perimeter = getPerimeter(radius)
area = getArea(radius)
print(f"El perímetro del círculo es: {perimeter}. Su área es {area}")