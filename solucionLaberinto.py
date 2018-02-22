#!/usr/bin/python

class JuegoLaberinto:
 def __init__(self):
   self.laberinto=None
 def obtenerHabitacion(self,id):
   return self.laberinto.obtenerHabitacion(id)

class Laberinto:
	def __init__(self):
		self.habitaciones=list()

	def agregarHabitacion(self,hab):
		self.habitaciones.append(hab)

	def obtenerHabitacion(self,id):
		for item in self.habitaciones:
			if item.id==id:
				return item
		print "no encontrado"

class ElementoMapa:
	def entrar(self):
		print "metodo a sobreescribir"
	def esPuerta(self):
		return False
	def esPared(self):
		return False
	def esHabtiacion(self):
		return False
	def esBomba(self):
		return False

class Contenedor(ElementoMapa):
	def __init__(self):
		self.hijos=list()

	def agregarHijo(self,unEM):
		self.hijos.append(unEM)

	def eliminarHijo(self,unEM):
		self.hijos.remove(unEM)

class Habitacion(Contenedor):
	def __init__(self,id):
		self.id=id
		self.norte=Pared()
		self.este=Pared()
		self.sur=Pared()
		self.oeste=Pared()
		self.hijos=list()

	def entrar(self):
		print "Estas en la habitacion-"+repr(self.id)
	def esHabitacion(self):
		return True

class Hoja(ElementoMapa):
	def entrar(self):
		print "es una hoja"

class Armario(Contenedor):
	def esArmario(self):
		return False
	def entrar(self):
		print "estas en un armario"

class Pared(Hoja):
	def entrar(self):
		print "Te has chocado con una pared"
	def esPared(self):
		return True

class Puerta(Hoja):
	def __init__(self, h1,h2):
		self.h1=h1
		self.h2=h2
		self.abierta=False
	def entrar(self):
		if self.abierta:
			print "Puerta abierta"
		else:
			print "Puerta cerrada"
	def esPuerta(self):
		return True

class Decorator(Hoja):
	def __init__(self):
		self.componente=None

class Bomba(Decorator):
	def __init__(self,estrategia):
		self.activa=False
		self.estrategia=estrategia

	def entrar(self):
		self.estrategia.entrar(self)

	def esBomba(self):
		return True

class Estrategia:
	def entrar(self,bomba):
		if bomba.activa:
			self.imprimir()
		else:
			bomba.componente.entrar()

	def imprimir(self):
		print "sobreescribir mensaje"

class Broma(Estrategia):
	def imprimir(self):
		print "bomba broma"

class H(Estrategia):
	def imprimir(self):
		print "bomba H"

class Mina(Estrategia):
	def imprimir(self):
		print "bomba mina"

class Orientacion:
	def poner(self,elemento,habitacion):
		print "sobreescribir"
class Norte(Orientacion):
	def poner(self,elemento,habitacion):
		habitacion.norte=elemento
class Sur(Orientacion):
	def poner(self,elemento,habitacion):
		habitacion.sur=elemento
class Este(Orientacion):
	def poner(self,elemento,habitacion):
		habitacion.este=elemento
class Oeste(Orientacion):
	def poner(self,elemento,habitacion):
		habitacion.oeste=elemento

# juego=JuegoLaberinto()

# lab=Laberinto()
# hab1=Habitacion(1)
# hab2=Habitacion(2)
# puerta=Puerta(hab1,hab2)
# lab.agregarHabitacion(hab1)
# lab.agregarHabitacion(hab2)
# juego.lab=lab

# hab=juego.obtenerHabitacion(1)
# hab.entrar()
# hab.norte.entrar()