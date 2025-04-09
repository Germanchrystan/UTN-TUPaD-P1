def esInputValido(strInput: str) -> bool:
  try:
    float(strInput)
  except ValueError:
    return False

  return float(strInput) >= 0

inputValido = False
magnitudStr: str
magnitud: float
escala: str

while not inputValido:
  magnitudStr = input("Ingrese magnitud del terremoto: ")
  if esInputValido(magnitudStr):
    inputValido = True
    magnitud = float(magnitudStr)
  else: 
    print("Magnitud no válida.")

if magnitud < 3:
  escala = "Muy leve"
if magnitud >= 3 and magnitud < 4:
  escala = "Leve"
if magnitud >= 4 and magnitud < 5:
  escala = "Moderado"
if magnitud >= 5 and magnitud < 6:
  escala = "Fuerte"
if magnitud >= 6 and magnitud < 7:
  escala = "Muy Fuerte"
if magnitud >= 7:
  escala = "Extremo"

print(f"Escala: {escala}")