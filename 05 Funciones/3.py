def informacion_personal(nombre, apellido, edad, residencia):
  print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

def es_edad_valida(intInput: str) -> bool:
  return intInput.isnumeric() and int(intInput) >= 0

def obtener_edad() -> int:
  ageInput: int
  validInput = False
  while not validInput:
    ageInput = input(f"Ingrese su edad: ")
    if es_edad_valida(ageInput):
      validInput = True
    else:
      print(f"Edad no válida.")
  return int(ageInput)


def obtener_valor_str(tipoDato: str):
  return input(f"Ingrese su {tipoDato}: ")
  

nombre = obtener_valor_str("nombre")
apellido = obtener_valor_str("apellido")
edad = obtener_edad()
residencia = obtener_valor_str("residencia")

informacion_personal(nombre, apellido, edad, residencia)