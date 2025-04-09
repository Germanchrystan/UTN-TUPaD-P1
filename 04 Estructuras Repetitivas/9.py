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

sum = 0

for i in range (0, LIMIT):
  num = inputNumber()
  sum += num
  
print(f"Media: {sum / LIMIT}")
