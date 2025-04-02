def isFloat(intInput: str) -> bool:
  try:
    return float(intInput) > 0
  except ValueError:
    return False

def getCelsius() -> float:
  intInput = 0
  while True:
    intInput = input(f"Ingrese los grados en celsius: ")
    if isFloat(intInput):
      return float(intInput)
    else:
      print("input no válido")

def getFahrenheit(celsius: float, precision: int) -> float:
  return round(celsius * 9 / 5 + 32, precision)

celsius = getCelsius()
fahrenheit = getFahrenheit(celsius, 2)
print(f"Los grados en fahrenheit son: {fahrenheit}")
