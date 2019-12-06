import unittest
from orcamento import Orcamento, Item
from impostos import ISS, ICMS

class TestISS(unittest.TestCase):

    def setUp(self):
        self.item = Item('bolsa', 200)
        self.orcamento = Orcamento()
        self.orcamento.adiciona_item(self.item)

    def test_calcula_ISS(self):
        iss = ISS()
        self.assertEqual(iss.calcula(self.orcamento), 200*0.1)
    
    def test_calcula_ICMS(self):
        icms = ICMS()
        self.assertEqual(icms.calcula(self.orcamento), 200*0.06)


if __name__ == '__main__':
    unittest.main()