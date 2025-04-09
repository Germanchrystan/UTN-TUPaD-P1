passInput: str
passLength: int
validInput = False

while not validInput:
  passInput = input("Ingrese su contraseña: ")
  passLength = len(passInput)
  validInput = passLength >= 8 and passLength <= 14
  if validInput:
    print("Ha ingresado una contraseña correcta")
  else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

