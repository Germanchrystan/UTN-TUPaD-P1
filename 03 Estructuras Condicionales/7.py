frase = input("Ingrese una frase: ")
longitud = len(frase)
vocales = ["a", "e", "i", "o", "u"]
final = frase[longitud  - 1].lower()

if final in vocales:
  frase += "!"

print(frase)