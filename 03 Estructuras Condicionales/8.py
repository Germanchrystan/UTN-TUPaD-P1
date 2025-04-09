opciones = ["1", "2", "3"]
resultado: str

nombre = input("Ingrese su nombre: ")
esOpcionValida = False
opcion: int

while not esOpcionValida:
  opcion = input("Ingrese una opcion (1, 2, 3): ")
  if opcion in opciones:
    esOpcionValida = True
  else:
    print("Opción inválida")

if opcion == "1":
  resultado = nombre.upper()
if opcion == "2":
  resultado = nombre.lower()
if opcion == "3":
  resultado = nombre.title()

print(f"Resultado: {resultado}")