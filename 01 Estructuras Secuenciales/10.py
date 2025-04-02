def isValidInt(intInput: str) -> bool:
  return intInput.isnumeric()

def getNum(index: int) -> int:
  intInput = 0
  while True:
    intInput = input(f"Ingrese el número {index}: ")
    if intInput.isnumeric():
      return int(intInput)
    else:
      print("input no válido")

arr = []
for i in range(3):
  arr.append(getNum(i + 1))

promedio = round(sum(arr) / len(arr), 2)
print(f"El promedio de los números es: {promedio}")