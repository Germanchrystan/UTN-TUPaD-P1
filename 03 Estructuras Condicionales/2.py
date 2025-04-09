def isValidGrade(intInput: str) -> bool:
  return intInput.isnumeric() and int(intInput) >= 0 and int(intInput) <= 10

def getGrade() -> int:
  gradeInput: int
  validInput = False
  while not validInput:
    gradeInput = input(f"Ingrese su nota: ")
    if isValidGrade(gradeInput):
      validInput = True
    else:
      print(f"Nota no válida.")

  return int(gradeInput)

grade = getGrade()

if grade >= 6:
  print("Aprobado")
else:
  print("Desaprobado")