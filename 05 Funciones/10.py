def isValidInt(intInput: str) -> bool:
  return intInput.isnumeric()

def getNum(index: int) -> int:
  intInput = 0
  validInput = False
  while not validInput:
    intInput = input(f"Ingrese el número {index}: ")
    if intInput.isnumeric():
      validInput = True
    else:
      print("input no válido")
  return int(intInput)

def calcular_promedio(num1, num2, num3):
  return round(sum((num1, num2, num3)) / 3, 2)

arr = []
for i in range(3):
  arr.append(getNum(i + 1))

print(f"El promedio de los números es: {calcular_promedio(arr[0],arr[1],arr[2])}")