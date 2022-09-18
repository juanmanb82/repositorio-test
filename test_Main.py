"""
    Probar las funciones con unittest
  
"""
import unittest
# Importamos nuestras funciones, esto puede cambiar de acuerdo a tus necesidades,
# aquí pongo un ejemplo
from main import *


class TestOperaciones(unittest.TestCase):
    def setUp(self):
        # Aquí, opcionalmente, ejecuta lo que deberías ejecutar antes
        # de comenzar cada test.
        pass

    def test_suma(self):
        esperado = 3
        actual = suma(1, 2)
        # Pásalo en el orden: actual, esperado
        self.assertEqual(actual, esperado)

    def test_resta(self):
        esperado = 5
        actual = resta(10, 5)
        # Pásalo en el orden: actual, esperado
        self.assertEqual(actual, esperado)

    def test_multiplicacion(self):
        esperado = 50
        actual = multiplicacion(10, 5)
        # Pásalo en el orden: actual, esperado
        self.assertEqual(actual, esperado)

    def test_division(self):
        esperado = 6
        actual = division(12, 2)
        # Pásalo en el orden: actual, esperado
        self.assertEqual(actual, esperado)

    def test_llamadaAPI(self):
        esperado = 35
        actual = pruebaLlamadaAPI()
        self.assertEqual(esperado,actual)



    def tearDown(self):
        # Aquí lo contrario de setUp, cuando cada test ha terminado
        pass


if __name__ == '__main__':
    unittest.main()