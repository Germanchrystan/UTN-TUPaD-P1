def isValidInt(strInput: str):
  try:
    int(strInput)
  except ValueError:
    return False
  return int(strInput) >= 0

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

invertedStr = ""
num = inputNumber()

while num != 0:
  digit = num % 10
  num = int(num / 10)
  invertedStr += str(digit)

result = int(invertedStr)

print(f"Resultado: {result}")