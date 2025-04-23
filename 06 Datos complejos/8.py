class Nodo:
  def __init__(self, valor):
    self.valor = valor
    self.__siguiente = None
  
  def setSiguiente(self, siguiente):
    self.__siguiente = siguiente
  
  def getSiguiente(self):
    return self.__siguiente

class Lista:
  def __init__(self):
    self.__cabeza = None
  
  def insertar(self, nodo: Nodo):
    nodo.setSiguiente(self.__cabeza)
    self.__cabeza = nodo
  
  def recorrer(self):
    prox = self.__cabeza
    contador = 1
    while prox != None:
      print(f"Nodo Nº{contador}. Valor: {prox.valor}")
      prox = prox.getSiguiente()
      contador += 1
  
  def invertir(self, nodoPrevio = None):
    siguiente = nodoPrevio.getSiguiente()
    if siguiente == None:
      self.__cabeza = nodoPrevio
      return nodoPrevio
    
    siguiente.setSiguiente(nodoPrevio)


"""
A B C

A tiene siguiente? Si
  B tiene siguiente? Si
    C tiene siguiente? No
    C es cabeza
    B (previo) es siguiente  
  A es siguiente
"""

lista = Lista()
lista.insertar(Nodo("A"))
lista.insertar(Nodo("B"))
lista.invertir()
lista.recorrer()
  

