def es_int_valido(intInput: str) -> bool:
  return intInput.isnumeric() and int(intInput) != 0

def obtener_num() -> int:
  intInput = 0
  inputValido = False
  while not inputValido:
    intInput = input("Ingrese un número: ")
    if es_int_valido(intInput):
      inputValido = True
    else:
      print("input no válido")
  return int(intInput)

def tabla_multiplicar(numero):
  for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

num = obtener_num()
tabla_multiplicar(num)
