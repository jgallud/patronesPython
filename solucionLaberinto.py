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

class Pared(ElementoMapa):
	def entrar(self):
		print "Te has chocado con una pared"

class Puerta(ElementoMapa):
	def __init__(self, h1,h2):
		self.h1=h1
		self.h2=h2
		self.abierta=False
	def entrar(self):
		if self.abierta:
			print "Puerta abierta"
		else:
			print "Puerta cerrada"

class Habitacion(ElementoMapa):
	def __init__(self,id):
		self.id=id
		self.norte=Pared()
		self.este=Pared()
		self.sur=Pared()
		self.oeste=Pared()
	def entrar(self):
		print "Estas en la habitacion-"+repr(self.id)

class Decorator(ElementoMapa):
	def __init__(self):
		self.componente=None

class Bomba(Decorator):
	def __init__(self):
		self.activa=False
	def entrar(self):
		if self.activa:
			print "Has explotado"
		else:
			self.componente.entrar()

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