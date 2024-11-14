import unittest

def multi(a,b):
    return a*b

def divisao(a,b):
    return a/b

class Test(unittest.TestCase):
    

    def test_multiplicacao(self):
        self.assertEqual(multi(2, 3), 6)
        self.assertEqual(multi(-1, 1), -1)
        self.assertEqual(multi(0, 0), 0)
        self.assertEqual(multi(5, 3), 15)

    def test_divisao(self):
        self.assertEqual(divisao(24, 2), 12)
        self.assertEqual(divisao(15, -3), -5)
        self.assertEqual(divisao(5, 0), 0)
        self.assertEqual(divisao(12, 3), 4)

if __name__ == '__main__':
    unittest.main()