import morse
import unittest

class TestMorse(unittest.TestCase):
    # def test_encode_us(self):
    #     self.assertEqual( morse.encode('us'), '..- ...')
        
    # def test_encode_u(self):
    #     self.assertEqual( morse.encode('u'), '..-')
    # def test_decode_us(self):
    #     self.assertEqual( morse.decode('..- ..'), 'us')



    def test_insertnode(self):
        tree = morse.Node("A")
        tree = morse.insert_node(tree,"B")
        tree = morse.insert_node(tree,"D")

        self.assertEqual(tree.left.value, "B")
        self.assertEqual(tree.right.value, "D")
    def test_insertnode_fail(self):
        tree = morse.Node("ST")
        tree = morse.insert_node(tree,"B")
        # Assert insertnode fail
        self.assertEqual(tree.left.value, "A")
        self.assertEqual(tree.right.value, "AB")
    def test_assertdeletion(self):
        # print("Before Deletion, Value = ",morse.MorseTree.right.value) # value = T
        morse.delete(morse.MorseTree,"T") 
        self.assertEqual(morse.MorseTree.right.value, "T")

    def test_assertion_find(self):
        tree = morse.Node("S")
        tree = morse.insert_node(tree,"B")
        tree= morse.insert_node(tree, "D")

        result = morse.find(tree, "B")
        # Assert find node
        self.assertEqual(result, True)
    
    def test_assertion_find_fail(self):
        tree = morse.Node("H")
        tree = morse.insert_node(tree,"Q")
        tree= morse.insert_node(tree, "D")

        result = morse.find(tree, "S")
        # Assert find node
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()