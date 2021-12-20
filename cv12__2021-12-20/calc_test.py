import unittest
import calc

class TestCalculate(unittest.TestCase):
    '''Testy pro řetězovou sčítačku'''

    def test_emptystring(self):
        '''Prázdný řetězec -> 0'''
        self.assertEqual(calc.calculate(""), 0)
    
    def test_single_number(self):
        '''Jedno číslo na vstupu -> hodnota čísla'''
        self.assertEqual(calc.calculate("12"), 12)
    
    def test_two_numbers(self):
        '''Více čísel oddělených čárkou -> součet čísel'''
        self.assertEqual(calc.calculate("5,6"), 11)
