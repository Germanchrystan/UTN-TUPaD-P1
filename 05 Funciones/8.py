def es_float_positivo(intInput: str) -> bool:
  try:
    return float(intInput) > 0
  except ValueError:
    return False

def obtener_valor(strDataType: str) -> float:
  inputValido = False
  while not inputValido:
    intInput = input(f"Ingrese su {strDataType}: ")
    if es_float_positivo(intInput):
      inputValido = True
    else:
      print("input no válido")
  return float(intInput)

def calcular_imc(altura: float, peso: float) -> float:
    return round(peso / (altura ** 2), 2)

peso = obtener_valor("peso")
altura = obtener_valor("altura")
imc = calcular_imc(altura, peso)
print(f"El IMC es: {imc}")