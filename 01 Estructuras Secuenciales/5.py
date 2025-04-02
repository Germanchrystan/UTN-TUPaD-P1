def isValidInt(intInput: int) -> bool:
  return intInput.isnumeric() and int(intInput) > 0

def getSeconds() -> int:
  intInput = 0
  while True:
    intInput = input("Ingrese la cantidad de segundos: ")
    if isValidInt(intInput):
      return int(intInput)
    else:
      print("input no válido")

segundos = getSeconds()
hours = segundos // 3600

print(f"La cantidad de horas es: {hours}")