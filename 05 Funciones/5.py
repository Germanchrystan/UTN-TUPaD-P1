def es_input_valido(intInput: int) -> bool:
  return intInput.isnumeric() and int(intInput) > 0

def obtener_segundos() -> int:
  intInput = 0
  while True:
    intInput = input("Ingrese la cantidad de segundos: ")
    if es_input_valido(intInput):
      return int(intInput)
    else:
      print("input no válido")

def segundos_a_horas(segunds):
  return segundos // 3600

segundos = obtener_segundos()
horas = segundos_a_horas(segundos)

print(f"La cantidad de horas es: {horas}")