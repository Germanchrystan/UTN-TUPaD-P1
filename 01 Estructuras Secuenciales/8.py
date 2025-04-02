def isPositiveFloat(intInput: str) -> bool:
  try:
    return float(intInput) > 0
  except ValueError:
    return False

def getValue(strDataType: str) -> float:
  while True:
    intInput = input(f"Ingrese su {strDataType}: ")
    if isPositiveFloat(intInput):
      return float(intInput)
    else:
      print("input no válido")

def getIMC(altura: float, peso: float) -> float:
    return round(peso / (altura ** 2), 2)

peso = getValue("peso")
altura = getValue("altura")
imc = getIMC(altura, peso)
print(f"El IMC es: {imc}")