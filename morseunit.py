import morse
import unittest

class TestMorse(unittest.TestCase):
    def test_encode_us(self):
        self.assertEqual( morse.encode('us'), '..- ...')
        
    def test_encode_u(self):
        self.assertEqual( morse.encode('u'), '..-')
    def test_decode_us(self):
        self.assertEqual( morse.decode('..- ..'), 'us')

if __name__ == '__main__':
    unittest.main()