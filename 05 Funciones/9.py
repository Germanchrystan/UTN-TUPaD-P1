def esFloat(intInput: str) -> bool:
  try:
    return float(intInput) > 0
  except ValueError:
    return False

def obtener_celsius() -> float:
  intInput = 0
  inputValido = False
  while not inputValido:
    intInput = input(f"Ingrese los grados en celsius: ")
    if esFloat(intInput):
      inputValido = True
    else:
      print("input no válido")
  return float(intInput)

def celsius_a_fahrenheit(celsius: float) -> float:
  return round(celsius * 9 / 5 + 32, 2)

celsius = obtener_celsius()
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"Los grados en fahrenheit son: {fahrenheit}")
