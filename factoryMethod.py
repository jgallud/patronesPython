from solucionLaberinto import *


class CreaLab(object):
	def __init__(self):
		self.lab=None
	def fabricarJuego(self):
		return JuegoLaberinto()
	
	def fabricarLaberinto(self):
		return Laberinto()
	
	def fabricarPared(self):
		return Pared()
	
	def fabricarPuerta(self, hab1,hab2):
		return Puerta(hab1,hab2)		
	
	def fabricarHabitacion(self,id):
		return Habitacion(id)
	
	def fabricarBomba(self,estrategia):
		return Bomba(estrategia)

	def crearLaberinto2Hab(self):
		self.lab=self.fabricarLaberinto()
		hab1=self.fabricarHabitacion(1)
		hab2=self.fabricarHabitacion(2)
		pt=self.fabricarPuerta(hab1,hab2)
		hab1.norte=pt
		hab2.sur=pt
		self.lab.agregarHabitacion(hab1)
		self.lab.agregarHabitacion(hab2)
		return self.lab


class CreaLabBomba(CreaLab):
	def crearLaberinto2Hab(self):
		self.lab=self.fabricarLaberinto()
		hab1=self.fabricarHabitacion(1)
		hab2=self.fabricarHabitacion(2)
		pt=self.fabricarPuerta(hab1,hab2)
		bomba1=self.fabricarBomba(Broma())
		bomba1.componente=self.fabricarPared()
		bomba2=self.fabricarBomba(Mina())
		bomba2.componente=self.fabricarPared()
		hab1.norte=pt
		hab1.este=bomba1
		hab2.sur=pt
		hab2.este=bomba2
		self.lab.agregarHabitacion(hab1)
		self.lab.agregarHabitacion(hab2)
		return self.lab

# Creator crea un laberinto normal
# fm=Creator()
# juego=fm.fabricarJuego()
# juego.laberinto=fm.crearLaberinto2Hab()

# hab=juego.obtenerHabitacion(1)
# hab.entrar()
# hab.norte.entrar()

#CreatorBomba crea un laberinto con 2 bombas
fm=CreaLabBomba()
juego=fm.fabricarJuego()
juego.laberinto=fm.crearLaberinto2Hab()
juego.laberinto=fm.crearLaberinto2Hab()

hab=juego.obtenerHabitacion(1)
hab.entrar()
hab.norte.entrar()

#abrimos la puerta y entramos
hab.norte.abierta=True
hab.norte.entrar()

#Aqui hay una bomba pero esta desactivada
hab.este.entrar()
#activo la bomba y exploto al entrar
hab.este.activa=True
hab.este.entrar()