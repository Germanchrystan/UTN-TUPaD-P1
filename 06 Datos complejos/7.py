class Cliente:
  def __init__(self, nombre: str, numero: str):
    self.__nombre = nombre
    self.__numero = numero
  
  def Nombre(self):
    return self.__nombre
  def Numero(self):
    return self.__numero

class Cola:
  def __init__(self):
    self.__turnos = []
  
  def encolar(self, cliente):
    self.__turnos.insert(0, cliente)
  
  def desencolar(self):
    try:
      self.__turnos.pop(0)
    except IndexError:
      print("No hay clientes aún")
  
  def siguiente(self):
    try:
      return self.__turnos[0]
    except IndexError:
      print("No hay clientes aún")


cola = Cola()
cola.desencolar()
cola.encolar(Cliente("Ger", "12345"))
siguiente = cola.siguiente()
print(f"El siguiente cliente es el numero {siguiente.Numero()}")

