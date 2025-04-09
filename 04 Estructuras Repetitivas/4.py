def isValidInt(strInput: str):
  try:
    int(strInput)
  except ValueError:
    return False
  return True

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

endCondition = False
num: int
result = 0

while not endCondition:
  num = inputNumber()
  result += num
  endCondition = num == 0

print(f"Resultado: {result}")