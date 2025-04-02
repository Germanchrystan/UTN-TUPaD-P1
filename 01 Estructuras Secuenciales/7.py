def isValidInt(intInput: str) -> bool:
  return intInput.isnumeric() and int(intInput) != 0

def getNum() -> int:
  intInput = 0
  while True:
    intInput = input(f"Ingrese un número: ")
    if isValidInt(intInput):
      return int(intInput)
    else:
      print("input no válido")

num1 = getNum()
num2 = getNum()

print(f"La suma de los números es: {num1 + num2}")
print(f"La resta de los números es: {num1 - num2}")
print(f"La multiplicación de los números es: {num1 * num2}")
print(f"La división de los números es: {num1 / num2}")