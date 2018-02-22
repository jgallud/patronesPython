import unittest
from factoryMethod import *

class TestLaberintoNormal(unittest.TestCase):
    """Test laberinto normal"""
    def setUp(self):
        self.juego=JuegoLaberinto()
        fm=CreaLab()
        self.juego.laberinto=fm.crearLaberinto2HabOrientaciones()

    def testJuego(self):
        """Test juego laberinto normal"""
        self.assertIsNot(self.juego.laberinto,None,"laberinto es nil")

    def testNumHabitaciones(self):
        """Test 2 habitaciones laberinto normal"""
        numHab=len(self.juego.laberinto.habitaciones)
        self.assertEqual(numHab,2,"el laberinto no tiene 2 habitaciones")

    def testHabitaciones(self):
        """Test puerta y paredes en habitaciones"""
        hab=self.juego.obtenerHabitacion(1)
        self.assertTrue(hab.norte.esPuerta())
        self.assertTrue(hab.este.esPared())
        self.assertTrue(hab.sur.esPared())
        self.assertTrue(hab.oeste.esPared())

class TestLaberintoBombas(unittest.TestCase):
    """Test laberinto con bombas"""
    def setUp(self):
        self.juego=JuegoLaberinto()
        fm=CreaLabBomba()
        self.juego.laberinto=fm.crearLaberinto2Hab()

    def testJuego(self):
        self.assertIsNot(self.juego.laberinto,None,"laberinto es nil")

    def testNumHabitaciones(self):
        numHab=len(self.juego.laberinto.habitaciones)
        self.assertEqual(numHab,2,"el laberinto no tiene 2 habitaciones")

    def testHabitaciones(self):
        hab=self.juego.obtenerHabitacion(1)
        self.assertTrue(hab.norte.esPuerta())
        self.assertTrue(hab.este.esBomba())
        self.assertTrue(hab.sur.esPared())
        self.assertTrue(hab.oeste.esPared())

        hab = self.juego.obtenerHabitacion(2)
        self.assertTrue(hab.sur.esPuerta())
        self.assertTrue(hab.este.esBomba())
        self.assertTrue(hab.norte.esPared())
        self.assertTrue(hab.oeste.esPared())

class TestLaberintoArmarios(unittest.TestCase):
    """Test laberinto con bombas"""
    def setUp(self):
        self.juego=JuegoLaberinto()
        fm=CreaLab()
        self.juego.laberinto=fm.crearLaberintoArmarios()

    def testJuego(self):
        self.assertIsNot(self.juego.laberinto,None,"laberinto es nil")

    def testNumHabitaciones(self):
        numHab=len(self.juego.laberinto.habitaciones)
        self.assertEqual(numHab,2,"el laberinto no tiene 2 habitaciones")

    def testHabitaciones(self):
        hab=self.juego.obtenerHabitacion(1)
        self.assertTrue(hab.norte.esPuerta())
        self.assertTrue(hab.este.esPared())
        self.assertTrue(hab.sur.esPared())
        self.assertTrue(hab.oeste.esPared())

        hab = self.juego.obtenerHabitacion(2)
        self.assertTrue(hab.sur.esPuerta())
        self.assertTrue(hab.este.esPared())
        self.assertTrue(hab.norte.esPared())
        self.assertTrue(hab.oeste.esPared())

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

if __name__ == '__main__':
    # Run only the tests in the specified classes

    test_classes_to_run = [TestLaberintoNormal,TestLaberintoBombas,TestLaberintoArmarios]

    loader = unittest.TestLoader()

    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    big_suite = unittest.TestSuite(suites_list)

    runner = unittest.TextTestRunner()
    results = runner.run(big_suite)