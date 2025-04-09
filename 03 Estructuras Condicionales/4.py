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

category: str
age = getAge()

if age < 12:
  category = "Niño/a"
elif age >= 12 and age < 18:
  category = "Adolescente"
elif age >= 18 and age < 30:
  category = "Adulto/a joven"
else:
  category = "Adulto/a"

print(f"Categoría: {category}")
