import unittest
from factoryMethod import *
from laberintoBuilder import *

class TestLaberintoNormal(unittest.TestCase):
    """Test laberinto normal"""
    def setUp(self):
        self.juego=JuegoLaberinto()
        fm=AbstractFactoryLaberinto()
        self.juego.laberinto=fm.crearLaberinto2HabOrientaciones()

    def testJuego(self):
        """Test juego laberinto normal"""
        self.assertIsNot(self.juego.laberinto,None,"laberinto es nil")

    def testNumHabitaciones(self):
        """Test 2 habitaciones laberinto normal"""
        numHab=len(self.juego.laberinto.hijos)
        self.assertEqual(numHab,2,"el laberinto no tiene 2 habitaciones")

    def testHabitaciones(self):
        """Test puerta y paredes en habitaciones"""
        hab=self.juego.obtenerHabitacion(1)
        forma=hab.forma
        self.assertTrue(forma.norte.esPuerta())
        self.assertTrue(forma.este.esPared())
        self.assertTrue(forma.sur.esPared())
        self.assertTrue(forma.oeste.esPared())

class TestLaberintoAbstractFactory(unittest.TestCase):
    """Test laberinto normal"""
    def setUp(self):
        self.juego=JuegoLaberinto()
        af=AbstractFactoryLaberinto()
        #self.juego.laberinto=fm.crearLaberinto2HabOrientaciones()
        self.juego.crearLaberinto2Hab(af)

    def testJuego(self):
        """Test juego laberinto normal"""
        self.assertIsNot(self.juego.laberinto,None,"laberinto es nil")

    def testNumHabitaciones(self):
        """Test 2 habitaciones laberinto normal"""
        numHab=len(self.juego.laberinto.hijos)
        self.assertEqual(numHab,2,"el laberinto no tiene 2 habitaciones")

    def testHabitaciones(self):
        """Test puerta y paredes en habitaciones"""
        hab=self.juego.obtenerHabitacion(1)
        forma=hab.forma
        self.assertTrue(forma.norte.esPuerta())
        self.assertTrue(forma.este.esPared())
        self.assertTrue(forma.sur.esPared())
        self.assertTrue(forma.oeste.esPared())

class TestLaberintoBombas(unittest.TestCase):
    """Test laberinto con bombas"""
    def setUp(self):
        self.juego=JuegoLaberinto()
        fm=AFLaberintoBomba()
        self.juego.laberinto=fm.crearLaberinto2Hab()

    def testJuego(self):
        self.assertIsNot(self.juego.laberinto,None,"laberinto es nil")

    def testNumHabitaciones(self):
        numHab=len(self.juego.laberinto.hijos)
        self.assertEqual(numHab,2,"el laberinto no tiene 2 habitaciones")

    def testHabitaciones(self):
        hab=self.juego.obtenerHabitacion(1)
        forma=hab.forma
        self.assertTrue(forma.norte.esPuerta())
        self.assertTrue(forma.este.esBomba())
        self.assertTrue(forma.sur.esPared())
        self.assertTrue(forma.oeste.esPared())

        hab = self.juego.obtenerHabitacion(2)
        forma=hab.forma
        self.assertTrue(forma.sur.esPuerta())
        self.assertTrue(forma.este.esBomba())
        self.assertTrue(forma.norte.esPared())
        self.assertTrue(forma.oeste.esPared())


class TestLaberintoArmarios(unittest.TestCase):
    """Test laberinto con bombas"""
    def setUp(self):
        self.juego=JuegoLaberinto()
        fm=AbstractFactoryLaberinto()
        self.juego.laberinto=fm.crearLaberintoArmarios()

    def testJuego(self):
        self.assertIsNot(self.juego.laberinto,None,"laberinto es nil")

    def testNumHabitaciones(self):
        numHab=len(self.juego.laberinto.hijos)
        self.assertEqual(numHab,2,"el laberinto no tiene 2 habitaciones")

    def testHabitaciones(self):
        hab=self.juego.obtenerHabitacion(1)
        forma=hab.forma
        self.assertTrue(forma.norte.esPuerta())
        self.assertTrue(forma.este.esPared())
        self.assertTrue(forma.sur.esPared())
        self.assertTrue(forma.oeste.esPared())

        hab = self.juego.obtenerHabitacion(2)
        forma=hab.forma
        self.assertTrue(forma.sur.esPuerta())
        self.assertTrue(forma.este.esPared())
        self.assertTrue(forma.norte.esPared())
        self.assertTrue(forma.oeste.esPared())

    def testArmarios(self):
        hab1 = self.juego.obtenerHabitacion(1)
        arm1=hab1.hijos[0]
        self.assertTrue(arm1.esArmario())

        hab2 = self.juego.obtenerHabitacion(2)
        arm2=hab2.hijos[0]
        self.assertTrue(arm2.esArmario())

    def testBombas(self):
        hab = self.juego.obtenerHabitacion(1)
        arm=hab.hijos[0]
        bm=arm.hijos[0]
        self.assertTrue(bm.esBomba())
        hab = self.juego.obtenerHabitacion(2)
        arm=hab.hijos[0]
        bm=arm.hijos[0]
        self.assertTrue(bm.esBomba())

class TestLaberintoBuilder(unittest.TestCase):
    """Test laberinto con bombas"""
    def setUp(self):
        director = Director()
        director.procesar('/soft/dev/laberintos/laberinto3.json')
        self.juego=director.builder.juego

    def testJuego(self):
        self.assertIsNot(self.juego.laberinto,None,"laberinto es nil")

    def testNumHabitaciones(self):
        numHab=len(self.juego.laberinto.hijos)
        self.assertEqual(numHab,2,"el laberinto no tiene 2 habitaciones")

    def testHabitaciones(self):
        hab=self.juego.obtenerHabitacion(1)
        forma=hab.forma
        self.assertTrue(forma.norte.esPuerta())
        self.assertTrue(forma.este.esPared())
        self.assertTrue(forma.sur.esPared())
        self.assertTrue(forma.oeste.esPared())

        hab = self.juego.obtenerHabitacion(2)
        forma=hab.forma
        self.assertTrue(forma.sur.esPuerta())
        self.assertTrue(forma.este.esPared())
        self.assertTrue(forma.norte.esPared())
        self.assertTrue(forma.oeste.esPared())

    def testArmarios(self):
        hab1 = self.juego.obtenerHabitacion(1)
        arm1=hab1.hijos[0]
        self.assertTrue(arm1.esArmario())

        hab2 = self.juego.obtenerHabitacion(2)
        arm2=hab2.hijos[0]
        self.assertTrue(arm2.esArmario())

    def testBombas(self):
        hab = self.juego.obtenerHabitacion(1)
        arm=hab.hijos[0]
        bm=arm.hijos[0]
        self.assertTrue(bm.esBomba())
        hab = self.juego.obtenerHabitacion(2)
        arm=hab.hijos[0]
        bm=arm.hijos[0]
        self.assertTrue(bm.esBomba())

class TestLaberintoEjercicio(unittest.TestCase):
    """Test laberinto con bombas"""
    def setUp(self):
        director = Director()
        director.procesar('/soft/dev/laberintos/laberintos/laberinto-ejercicio.json')
        self.juego=director.builder.juego

    def testJuego(self):
        self.assertIsNot(self.juego.laberinto,None,"laberinto es nil")

    def testNumHabitaciones(self):
        numHab=len(self.juego.laberinto.hijos)
        self.assertEqual(numHab,4,"el laberinto no tiene 2 habitaciones")

    def testHabitaciones(self):
        hab=self.juego.obtenerHabitacion(1)
        forma=hab.forma
        self.assertTrue(forma.norte.esPared())
        self.assertTrue(forma.este.esPared())
        self.assertTrue(forma.sur.esPuerta())
        self.assertTrue(forma.oeste.esPared())

        hab = self.juego.obtenerHabitacion(2)
        forma=hab.forma
        self.assertTrue(forma.sur.esPared())
        self.assertTrue(forma.este.esPuerta())
        self.assertTrue(forma.norte.esPuerta())
        self.assertTrue(forma.oeste.esPared())

        hab = self.juego.obtenerHabitacion(3)
        forma=hab.forma
        self.assertTrue(forma.sur.esPuerta())
        self.assertTrue(forma.este.esPared())
        self.assertTrue(forma.norte.esPared())
        self.assertTrue(forma.oeste.esPuerta())

        hab = self.juego.obtenerHabitacion(4)
        forma=hab.forma
        self.assertTrue(forma.sur.esPared())
        self.assertTrue(forma.este.esPared())
        self.assertTrue(forma.norte.esPuerta())
        self.assertTrue(forma.oeste.esPared())


    def testArmarios(self):
        hab1 = self.juego.obtenerHabitacion(1)
        arm1=hab1.hijos[0]
        self.assertTrue(arm1.esArmario())

        hab2 = self.juego.obtenerHabitacion(2)
        arm2=hab2.hijos[0]
        self.assertTrue(arm2.esArmario())

        hab3 = self.juego.obtenerHabitacion(3)
        arm3 = hab3.hijos[0]
        self.assertTrue(arm2.esArmario())

        hab4 = self.juego.obtenerHabitacion(4)
        arm4 = hab4.hijos[0]
        self.assertTrue(arm4.esArmario())

    def testBombas(self):
        hab = self.juego.obtenerHabitacion(1)
        arm=hab.hijos[0]
        bm=arm.hijos[0]
        self.assertTrue(bm.esBomba())
        self.assertTrue(bm.estrategia.esMina())

        hab = self.juego.obtenerHabitacion(3)
        bm=hab.hijos[1]
        self.assertTrue(bm.esBomba())
        self.assertTrue(bm.estrategia.esH())

        hab = self.juego.obtenerHabitacion(4)
        arm=hab.hijos[0]
        bm=arm.hijos[0]
        self.assertTrue(bm.esBomba())
        self.assertTrue(bm.estrategia.esBroma())

if __name__ == '__main__':
    # Run only the tests in the specified classes

    test_classes_to_run = [TestLaberintoNormal,TestLaberintoAbstractFactory,TestLaberintoBombas,TestLaberintoArmarios,TestLaberintoBuilder, TestLaberintoEjercicio]

    loader = unittest.TestLoader()

    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    big_suite = unittest.TestSuite(suites_list)

    runner = unittest.TextTestRunner()
    results = runner.run(big_suite)