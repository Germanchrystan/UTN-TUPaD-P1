def isValidInt(intInput: str) -> bool:
  return intInput.isnumeric() and int(intInput) != 0

def getNum() -> int:
  intInput = 0
  inputValido = False
  while not inputValido:
    intInput = input(f"Ingrese un número: ")
    if isValidInt(intInput):
      inputValido = True
    else:
      print("input no válido")
  return int(intInput)

def operaciones_basicas(num1, num2):
  return (num1 + num2, num1 - num2, num1 * num2, num1 / num2)

num1 = getNum()
num2 = getNum()
resultados = operaciones_basicas(num1, num2)

print(f"La suma de los números es: {resultados[0]}")
print(f"La resta de los números es: {resultados[1]}")
print(f"La multiplicación de los números es: {resultados[2]}")
print(f"La división de los números es: {resultados[3]}")