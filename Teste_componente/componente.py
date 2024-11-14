import unittest

def soma(a, b):
    return a + b

def sub(a, b):
    return a - b 

def mult(a, b):
    return a * b

def div(a, b):
    return a / b

class Test(unittest.TestCase):
    
    def test_soma(self):
        self.assertEqual(soma(2, 3), 5)
        self.assertEqual(soma(-1, 1), 0)
        self.assertEqual(soma(0, 0), 0)
        

    def test_subtrai(self):
        self.assertEqual(sub(5, 3), 2)
        self.assertEqual(sub(0, 1), -1)
        self.assertEqual(sub(2, 2), 0)

    def test_mult(self):
        self.assertEqual(mult(5, 3), 15)
        self.assertEqual(mult(2, 2), 4)
        self.assertEqual(mult(5, 5), 25)

    def test_div(self):
        self.assertEqual(div(6, 3), 2)
        self.assertEqual(div(24, 6), 4)
        self.assertEqual(div(40, 10), 4)

        
if __name__ == '__main__':
    unittest.main()
