import unittest

def soma(a, b):
    return a + b

def sub(a, b):
    return a - b 

class Test(unittest.TestCase):
    
    def test_soma(self):
        self.assertEqual(soma(2, 3), 5)
        self.assertEqual(soma(-1, 1), 0)
        self.assertEqual(soma(0, 0), 0)
        
    def test_subtrai(self):
        self.assertEqual(sub(5, 3), 2)
        self.assertEqual(sub(0, 1), -1)
        self.assertEqual(sub(2, 2), 0)

if __name__ == '__main__':
    unittest.main()
