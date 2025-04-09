import random

def isValidInt(strInput: str):
  try:
    int(strInput)
  except ValueError:
    return False
  return True

def inputNumber()-> int:
  validInt = False
  strInput: str
  while not validInt:
    strInput = input("Ingrese un número: ")
    if isValidInt(strInput):
      validInt = True
    else:
      print("Input no válido.")
  return int(strInput)

secretNum = random.randrange(0,10)
guessed = False
tries = 0

while not guessed:
  guess = inputNumber()
  tries += 1
  if guess > secretNum:
    print("Más abajo!")
  elif guess < secretNum:
    print("Más arriba!")
  else:
    guessed = True

print(f"Adivinaste! Cantidad de intentos: {tries}")
