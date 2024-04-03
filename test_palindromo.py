import unittest

from palindromo import cant_palabras_palindromes, is_palindrome


class TestIsPalindrome(unittest.TestCase):
    def test_with_a(self):
        input = "a"
        result = is_palindrome(input)
        self.assertTrue(result)

    def test_with_ala(self):
        input = "ala"
        result = is_palindrome(input)
        self.assertTrue(result)

    def test_with_neuquen(self):
        input = "neuquen"
        result = is_palindrome(input)
        self.assertTrue(result)

    def test_with_Neuquen(self):
        input = "Neuquen"
        result = is_palindrome(input)
        self.assertTrue(result)

    def test_with_hola(self):
        input = "hola"
        result = is_palindrome(input)
        self.assertFalse(result)

class TestCantidadDePalabrasPalindromes(unittest.TestCase):
    def test_cantidad_de_palabras_palindromes_simple(self):
        palabras = ["ala"]
        resultado = cant_palabras_palindromes(palabras)
        self.assertEqual(resultado, 1)

    def test_cantidad_de_palabras_palindromes_con_2(self):
        palabras = ["ala", "neuquen"]
        resultado = cant_palabras_palindromes(palabras)
        self.assertEqual(resultado, 2)

    def test_cantidad_de_palabras_palindromes_con_3(self):
        palabras = ["ala", "neuquen", "hola"]
        resultado = cant_palabras_palindromes(palabras)
        self.assertEqual(resultado, 2)

    def test_cantidad_de_palabras_palindromes_con_4(self):
        palabras = ["ala", "neuquen", "hola", "programacion"]
        resultado = cant_palabras_palindromes(palabras)
        self.assertEqual(resultado, 2)

    def test_cantidad_de_palabras_palindromes_con_5(self):
        palabras = ["ala", "neuquen", "hola", "programacion", "palap"]
        resultado = cant_palabras_palindromes(palabras)
        self.assertEqual(resultado, 3)

    def test_cantidad_de_palabras_palindromes_complejo(self):
        palabras = ["ala", "neuquen", "hola", "programacion", "palap", "neu  quen"]
        resultado = cant_palabras_palindromes(palabras)
        self.assertEqual(resultado, 4)

    def test_cantidad_de_palabras_palindromes_complejo_2(self):
        palabras = [
            "Ala",
            "neuquen",
            "hola",
            "programacion",
            "palap",
            "Neu  quen",
            "agita falsos usos la fatiga",
            "presidente de la camara de diputados: martin menem",
        ]
        resultado = cant_palabras_palindromes(palabras)
        self.assertEqual(resultado, 5)


if __name__ == '__main__':
    unittest.main()