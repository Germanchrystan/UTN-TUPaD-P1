LIMIT = 100

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

evenQuantity = 0
oddQuantity = 0
positiveQuantity = 0
negativeQuantity = 0

for i in range (0, LIMIT):
  num = inputNumber()
  if num > 0:
    positiveQuantity += 1
  if num < 0:
    negativeQuantity += 1
  
  if num % 2 == 0:
    evenQuantity += 1
  else:
    oddQuantity += 1

print(f"Cantidad de números positivos: {positiveQuantity}")
print(f"Cantidad de números negativos: {negativeQuantity}")
print(f"Cantidad de números pares: {evenQuantity}")
print(f"Cantidad de números impares: {oddQuantity}")