def isValidInt(intInput: str) -> bool:
  return intInput.isnumeric() and int(intInput) != 0

def getNum() -> int:
  intInput = 0
  while True:
    intInput = input("Ingrese un número: ")
    if isValidInt(intInput):
      return int(intInput)
    else:
      print("input no válido")

num = getNum()
for i in range(1, 11):
  print(f"{num} x {i} = {num * i}")
