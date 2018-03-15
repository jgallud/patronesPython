from solucionLaberinto import *


class AbstractFactoryLaberinto(object):
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
		hab=Habitacion(id)
		hab.forma=self.fabricarForma()
		return hab
	
	def fabricarBomba(self,estrategia):
		return Bomba(estrategia)

	def fabricarArmario(self):
		return Armario()

	def fabricarForma(self):
		cuadrado=Cuadrado()
		cuadrado.orientaciones.append(Norte())
		cuadrado.orientaciones.append(Este())
		cuadrado.orientaciones.append(Sur())
		cuadrado.orientaciones.append(Oeste())
		return cuadrado

	def crearLaberinto2Hab(self):
		self.lab=self.fabricarLaberinto()
		hab1=self.fabricarHabitacion(1)
		hab2=self.fabricarHabitacion(2)
		pt=self.fabricarPuerta(hab1,hab2)
		hab1.norte=pt
		hab2.sur=pt
		self.lab.agregarHijo(hab1)
		self.lab.agregarHijo(hab2)
		return self.lab

	def crearLaberinto2HabOrientaciones(self):
		norte=Norte()
		sur=Sur()
		este=Este()
		oeste=Oeste()
		self.lab=self.fabricarLaberinto()
		hab1=self.fabricarHabitacion(1)
		hab2=self.fabricarHabitacion(2)
		pt=self.fabricarPuerta(hab1,hab2)
		hab1.ponerEn(norte, pt)
		hab2.ponerEn(sur, pt)

		hab1.ponerEn(este, self.fabricarPared())
		hab1.ponerEn(oeste, self.fabricarPared())
		hab1.ponerEn(sur, self.fabricarPared())

		hab2.ponerEn(este, self.fabricarPared())
		hab2.ponerEn(oeste, self.fabricarPared())
		hab2.ponerEn(norte, self.fabricarPared())

		self.lab.agregarHijo(hab1)
		self.lab.agregarHijo(hab2)
		return self.lab

	def crearLaberintoArmarios(self):
		norte = Norte()
		sur = Sur()
		este = Este()
		oeste = Oeste()
		self.lab = self.fabricarLaberinto()
		hab1 = self.fabricarHabitacion(1)
		hab2 = self.fabricarHabitacion(2)
		pt = self.fabricarPuerta(hab1, hab2)
		hab1.ponerEn(norte,pt)
		hab2.ponerEn(sur,pt)

		bomba1=self.fabricarBomba(Broma())
		bomba2=self.fabricarBomba(H())

		arm1=self.fabricarArmario()
		arm2=self.fabricarArmario()

		arm1.agregarHijo(bomba1)
		arm2.agregarHijo(bomba2)

		hab1.ponerEn(este,self.fabricarPared())
		hab1.ponerEn(oeste,self.fabricarPared())
		hab1.ponerEn(sur,self.fabricarPared())

		hab2.ponerEn(este,self.fabricarPared())
		hab2.ponerEn(oeste,self.fabricarPared())
		hab2.ponerEn(norte,self.fabricarPared())

		hab1.agregarHijo(arm1)
		hab2.agregarHijo(arm2)

		self.lab.agregarHijo(hab1)
		self.lab.agregarHijo(hab2)
		return self.lab

class AFLaberintoBomba(AbstractFactoryLaberinto):
	def crearLaberinto2Hab(self):
		norte = Norte()
		sur = Sur()
		este = Este()
		oeste = Oeste()
		self.lab=self.fabricarLaberinto()
		hab1=self.fabricarHabitacion(1)
		hab2=self.fabricarHabitacion(2)
		pt=self.fabricarPuerta(hab1,hab2)

		hab1.ponerEn(norte,pt)
		hab2.ponerEn(sur,pt)

		bomba1=self.fabricarBomba(Broma())
		bomba1.componente=self.fabricarPared()
		bomba2=self.fabricarBomba(Mina())
		bomba2.componente=self.fabricarPared()

		hab1.ponerEn(este, bomba1)
		hab2.ponerEn(este, bomba1)

		hab1.ponerEn(oeste, self.fabricarPared())
		hab1.ponerEn(sur, self.fabricarPared())

		hab2.ponerEn(oeste, self.fabricarPared())
		hab2.ponerEn(norte, self.fabricarPared())

		self.lab.agregarHijo(hab1)
		self.lab.agregarHijo(hab2)
		return self.lab

# Creator crea un laberinto normal
# af=AbstractFactoryLaberinto()
# juego=af.fabricarJuego()
# juego.laberinto=af.crearLaberintoArmarios()
#
# hab=juego.obtenerHabitacion(1)
# hab.entrar()
# hab.forma.norte.entrar()
#
# juego.laberinto.enumerar()

#CreatorBomba crea un laberinto con 2 bombas
# fm=CreaLabBomba()
# juego=fm.fabricarJuego()
# juego.laberinto=fm.crearLaberinto2Hab()
# juego.laberinto=fm.crearLaberinto2Hab()
#
# hab=juego.obtenerHabitacion(1)
# hab.entrar()
# hab.norte.entrar()
#
# #abrimos la puerta y entramos
# hab.norte.abierta=True
# hab.norte.entrar()
#
# #Aqui hay una bomba pero esta desactivada
# hab.este.entrar()
#
# #activo la bomba y exploto al entrar
# hab.este.activa=True
# hab.este.entrar()