#!/usr/bin/python
import time

class JuegoLaberinto:
 def __init__(self):
   	self.laberinto=None
	self.bichos=None
 def crearLaberinto2Hab(self,unAF):
	 norte = Norte()
	 sur = Sur()
	 este = Este()
	 oeste = Oeste()
	 lab = unAF.fabricarLaberinto()
	 hab1 = unAF.fabricarHabitacion(1)
	 hab2 = unAF.fabricarHabitacion(2)
	 pt = unAF.fabricarPuerta(hab1, hab2)
	 hab1.ponerEn(norte,pt)
	 hab2.ponerEn(sur,pt)
	 hab1.ponerEn(este, unAF.fabricarPared())
	 hab1.ponerEn(oeste, unAF.fabricarPared())
	 hab1.ponerEn(sur, unAF.fabricarPared())
	 hab2.ponerEn(este, unAF.fabricarPared())
	 hab2.ponerEn(oeste, unAF.fabricarPared())
	 hab2.ponerEn(norte, unAF.fabricarPared())
	 lab.agregarHijo(hab1)
	 lab.agregarHijo(hab2)
	 self.laberinto=lab

 def obtenerHabitacion(self,id):
   return self.laberinto.obtenerHabitacion(id)

 def agregarBicho(self,unBicho):
	 self.bichos.append(unBicho)

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
	def esArmario(self):
		return False
	def enumerar(self):
		pass
	def __repr__(self):
		pass

class Contenedor(ElementoMapa):
	def __init__(self):
		self.hijos=list()
		self.forma=None
	def agregarHijo(self,unEM):
		self.hijos.append(unEM)
	def eliminarHijo(self,unEM):
		self.hijos.remove(unEM)
	def ponerEn(self,unaOr,unEM):
		self.forma.ponerEn(unaOr,unEM)
	def enumerar(self):
		print repr(self)
		for e in self.hijos:
			e.enumerar()

class Forma:
	def __init__(self):
		self.orientaciones=list()
	def ponerEn(self,unaOr,unEM):
		unaOr.poner(unEM,self)

class Cuadrado(Forma):
	def __init__(self):
		self.norte=None
		self.este=None
		self.sur=None
		self.oeste=None
		Forma.__init__(self)

class Laberinto(Contenedor):
	def obtenerHabitacion(self,id):
		for item in self.hijos:
			if item.esHabitacion and item.id==id:
				return item
		print "no encontrado"
	def __repr__(self):
		return "Laberinto"

class Habitacion(Contenedor):
	def __init__(self,id):
		self.id=id
		Contenedor.__init__(self)
	def __repr__(self):
		return "Habitacion"
	def entrar(self):
		print "Estas en la habitacion-"+repr(self.id)
	def esHabitacion(self):
		return True

class Hoja(ElementoMapa):
	def entrar(self):
		print "es una hoja"
	def enumerar(self):
		print repr(self)

class Armario(Contenedor):
	def esArmario(self):
		return True
	def entrar(self):
		print "estas en un armario"
	def __repr__(self):
		return "Armario"

class Pared(Hoja):
	def entrar(self):
		print "Te has chocado con una pared"
	def esPared(self):
		return True
	def __repr__(self):
		return "Pared"

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
	def __repr__(self):
		return "Puerta"

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
	def __repr__(self):
		return "Bomba"

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
	def poner(self,elemento,forma):
		pass

class Norte(Orientacion):
	def poner(self,elemento,forma):
		forma.norte=elemento
class Sur(Orientacion):
	def poner(self,elemento,forma):
		forma.sur=elemento
class Este(Orientacion):
	def poner(self,elemento,forma):
		forma.este=elemento
class Oeste(Orientacion):
	def poner(self,elemento,forma):
		forma.oeste=elemento

class Bicho:
	def __init__(self):
		self.modo=None
		self.posicion=None
	def actua(self):
		self.modo.actua(self)

class Modo:
	def actua(self,unBicho):
		self.dormir
		self.caminar(unBicho)
	def dormir(self):
		time.sleep(2)
	def caminar(self,unBicho):
		pass

class Agresivo(Modo):
	def dormir(self):
		time.sleep(1)

class Perezoso(Modo):
	def dormir(self):
		time.sleep(3)

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