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
    
validNums = False
num1 = inputNumber()
num2 = inputNumber()
result = 0

for i in range(min(num1 + 1, num2 + 1), max(num1, num2)):
  result += i

print(f"Resultado: {result}")