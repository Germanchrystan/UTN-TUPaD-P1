def isValidAge(intInput: str) -> bool:
  return intInput.isnumeric() and int(intInput) >= 0

def getAge() -> int:
  ageInput: int
  validInput = False
  while not validInput:
    ageInput = input(f"Ingrese su edad: ")
    if isValidAge(ageInput):
      validInput = True
    else:
      print(f"Edad no válida.")

  return int(ageInput)

age = getAge()

if age > 18:
  print("Es mayor de edad")