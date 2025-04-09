def isValidNum(intInput: str) -> bool:
  return intInput.isnumeric() and int(intInput) >= 0 and int(intInput) <= 10

def isEven(intInput: int) -> bool:
  return intInput % 2 == 0

intInput: int
validInput = False
while not validInput:
  intInput = input(f"Ingrese un número: ")
  if isValidNum(intInput) and isEven(int(intInput)):
    print("Ha ingresado un número par")
    validInput = True
  else:
    print("Por favor, ingrese un número par")


  