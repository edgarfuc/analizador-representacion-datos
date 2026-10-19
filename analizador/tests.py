
from django.test import TestCase
from .views import analizar_numero, analizar_texto


class AnalizadorTests(TestCase):

    def test_decimal_a_binario(self):
        resultado = analizar_numero("10", 10)
        self.assertEqual(resultado["binario"], "1010")
        self.assertEqual(resultado["decimal"], 10)

    def test_hexadecimal_a_decimal(self):
        resultado = analizar_numero("2AF", 16)
        self.assertEqual(resultado["decimal"], 687)

    def test_binario_a_decimal(self):
        resultado = analizar_numero("1010", 2)
        self.assertEqual(resultado["decimal"], 10)

    def test_octal_a_decimal(self):
        resultado = analizar_numero("17", 8)
        self.assertEqual(resultado["decimal"], 15)

    def test_rechaza_numero_fuera_de_rango(self):
        with self.assertRaises(ValueError):
            analizar_numero("65536", 10)

    def test_rechaza_digito_invalido(self):
        with self.assertRaises(ValueError):
            analizar_numero("102", 2)

    def test_caracter_enie_utf8(self):
        resultado = analizar_texto("ñ")
        self.assertEqual(resultado[0]["decimal"], 241)
        self.assertEqual(resultado[0]["unicode"], "U+00F1")
        self.assertEqual(resultado[0]["utf8"], "C3 B1")

    def test_limite_de_texto(self):
        with self.assertRaises(ValueError):
            analizar_texto("A" * 21)
