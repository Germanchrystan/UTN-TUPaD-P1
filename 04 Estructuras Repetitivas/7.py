def isValidInt(strInput: str):
  try:
    int(strInput)
  except ValueError:
    return False
  return int(strInput) > 0

def inputNumber()-> int:
  validInt = False
  strInput: str
  while not validInt:
    strInput = input("Ingrese un número: ")
    if isValidInt(strInput):
      validInt = True
    else:
      print("Input no válido.")
  return int(strInput)

rangeMax = inputNumber()
result = 0

for i in range(0, rangeMax):
  result += i
  print(result)

print(f"Resultado: {result}")