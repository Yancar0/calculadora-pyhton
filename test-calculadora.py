# test_calculadora.py
import unittest
from calculadora import suma, resta, multiplicacion, division

class TestCalculadora(unittest.TestCase):

    # Prueba unitaria
    def test_suma(self):
        self.assertEqual(suma(3, 5), 8)
    
    def test_resta(self):
        self.assertEqual(resta(5, 2), 3)

    # Prueba de integración
    def test_operaciones_encadenadas(self):
        # (3 + 5) * 2 = 16
        resultado = multiplicacion(suma(3, 5), 2)
        self.assertEqual(resultado, 16)

    # Prueba de rendimiento
    def test_rendimiento(self):
        for _ in range(1000000):  # Un millón de operaciones
            suma(1, 2)
        # Si llega aquí sin errores, se considera exitosa
        self.assertTrue(True)

    # Extra: verificar división segura
    def test_division_por_cero(self):
        with self.assertRaises(ValueError):
            division(5, 0)


if __name__ == "__main__":
    unittest.main()
