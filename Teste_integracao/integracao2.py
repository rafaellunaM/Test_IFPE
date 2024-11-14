import unittest
import sqlite3

class Test(unittest.TestCase):

    def setUp(self):

        self.conn = sqlite3.connect(':memory:')
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE usuarios (id INTEGER PRIMARY KEY, nome TEXT, endereco TEXT, idade INT)")

    def test_inserir_usuario(self):

        self.cursor.execute("INSERT INTO usuarios (nome, endereco, idade) VALUES ('João','Rua da Aurora',16)")
        self.conn.commit()

        self.cursor.execute("INSERT INTO usuarios (nome, endereco, idade) VALUES ('Maria','Rua da Aurora',17)")
        self.conn.commit()

        self.cursor.execute("SELECT nome FROM usuarios WHERE id = 1")
        usuario = self.cursor.fetchone()
        self.assertEqual(usuario[0], 'João')

        self.cursor.execute("SELECT nome FROM usuarios WHERE idade = 16")
        usuario = self.cursor.fetchone()
        self.assertEqual(usuario[0], 'João')

        self.cursor.execute("SELECT nome FROM usuarios WHERE idade = 17")
        usuario = self.cursor.fetchone()
        self.assertEqual(usuario[0], 'Maria')


    def tearDown(self):
        return super().tearDown()
    
if __name__ == '__main__':
    unittest.main()
