import unittest

def mult(a, b):
    return a * b

def div(a, b):
    return a / b 

class Test(unittest.TestCase):
    
    def test_multiplica(self):
        self.assertEqual(mult(2, 3), 6)
        self.assertEqual(mult(-1, 1), -1)
        self.assertEqual(mult(0, 0), 0)
        
    def test_divide(self):
        self.assertEqual(div(6, 3), 2)
        self.assertEqual(div(10, 2), 5)
        self.assertEqual(div(2, 1), 2)

if __name__ == '__main__':
    unittest.main()
