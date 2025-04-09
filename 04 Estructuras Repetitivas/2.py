def isValidInt(strInput: str):
  try:
    int(strInput)
  except ValueError:
    return False
  return True

num: int
strInput: str
validInput: bool = False

while not validInput:
  strInput = input("Ingrese un número: ")
  validInput = isValidInt(strInput)

num = int(strInput)

digitQuantity = 0

while num != 0:
  num = int(num/10)
  digitQuantity += 1

print(f"Cantidad de dígitos: {digitQuantity}")
