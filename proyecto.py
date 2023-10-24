# HERENCIA DE DOS CLASES A UNA

# Definicion de la clase animal
class Animal:
  def _init_(self, nombre):
    self.nombre=nombre

  def hablar (self):
    pass  # funcion sin nada dentro para que no de error
 
  def comer(self):
    if isinstance (self, Acuatico):
      print(f"{self.nombre} come peces")
    else:
      if isinstance (self, Terrestre):
        print(f"{self.nombre} come gallinas")
      else:
        if isinstance (self, Anfibio):
          print(f"{self.nombre} come de todo")

# La clase Terrestre hereda de la clase animal
class Terrestre(Animal):
  def desplazamiento(self):
    print(f"{self.nombre} camina sobre la tierra")
 
  def hablar(self):
    print(f"{self.nombre} emite sonidos terrestres")
 
# La clase acuatico hereda de la clase animal
class Acuatico(Animal):
  def desplazamiento(self):
    print(f"{self.nombre} nada en el agua")
 
  def hablar(self):
    print(f"{self.nombre} emite sonidos acuaticos")

#  La clase anfibio hereda de Terrestre y Acuatico
class Anfibio(Terrestre, Acuatico):

  def hablar(self, tipo):
    if tipo == "tierra":
      super().hablar() #Super llama a terrestre por que esta declarado primero
      # Al hacer super lo estas llamando por herencia, si no lo llama de forma implicita
    else:
      Acuatico.hablar(self)

# Creamos un objeto de la clase Anfibio
rana = Anfibio("Rana")
lobo = Terrestre("Lobo")
pescao = Acuatico("Pescao")
print("El programa va a empezar")
# Llamado al metodo "desplazamiento" heredado de terrestre
rana.desplazamiento()
lobo.desplazamiento()
# Llamada al metodo "hablar" sobrecargado en la clase terrestre
rana.hablar("tierra") # salida: rana emite sonidos terrestres

# Llamada al metodo "Comer" en la clase animal
rana.comer()
lobo.comer()
pescao.comer()
print("El programa ha terminado")
