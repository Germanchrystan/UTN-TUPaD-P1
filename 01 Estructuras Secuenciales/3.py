def isValidStr(strInput: str) -> bool:
  return not(strInput.isnumeric()) and len(strInput) > 0
def isValidInt(intInput: int) -> bool:
  return intInput.isnumeric() and int(intInput) > 0

def getStringValue(strDataName: str) -> str:
  strInput = ""
  while True:
    strInput = input(f"Ingrese su {strDataName}: ")
    if isValidStr(strInput):
      return strInput
    else:
      print(f"{strDataName} no válido")

def getIntValue(intDataName: str) -> int:
  intInput = 0
  while True:
    intInput = input(f"Ingrese su {intDataName}: ")
    if isValidInt(intInput):
      return intInput
    else:
      print(f"{intDataName} no válido")

nombre = getStringValue("nombre")
apellido = getStringValue("apellido")
residencia = getStringValue("residencia")
edad = getIntValue("edad")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
