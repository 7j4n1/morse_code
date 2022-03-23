class TreeNode:
    def __init__(self, data, left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

class BTree(object):
    def __init__(self):
        self.root = None
        self.COUNT = [2]

    def insert_node(self, node, data, code):
        # check whether there is a sign
        if len(code) == 0:
            return TreeNode(data)
        
        if node == None:
            node = TreeNode("START")
        
        if code[0] == '-':
            # extract the rest of the sign
            node.right = self.insert_node(node.right, data, code[1:])
        elif code[0] == '.':
            node.left = self.insert_node(node.left, data, code[1:])

        return node
    # function to call to insert data into Morse Tree
    def insert(self, data, code):
        self.root = self.insert_node(self.root, data, code)

    def preorder(self, node, indent=0, prefix="r - "):
        '''
            Function to print tree in Pre Order Transversal Order
        '''
        if node == None:
            return
    
        indent += self.COUNT[0]
        for l in range(self.COUNT[0], indent):
            print(end = " ")
        # print the node value with appropriate indentation
        print(prefix + node.data)
        # process the left child(s)
        self.preorder(node.left, indent,prefix="l - ")
        # process right child(s)
        self.preorder(node.right, indent, prefix="r - ")

    def show(self):
        '''
        Function to call to print Morse Binary Tree in PREORDER STACK
        '''
        self.preorder(self.root)


if __name__ == '__main__':
    mbt = BTree()
    # 1ST LEVEL
    mbt.insert("E", ".")
    mbt.insert("T", "-")
    # 2ND LEVEL
    mbt.insert("I", "..")
    mbt.insert("A", ".-")
    mbt.insert("N", "-.")
    mbt.insert("M", "--")
    # 3RD LEVEL
    mbt.insert("S", "...")
    mbt.insert("U", "..-")
    mbt.insert("R", ".-.")
    mbt.insert("W", ".--")
    mbt.insert("D", "-..")
    mbt.insert("K", "-.-")
    mbt.insert("G", "--.")
    mbt.insert("O", "---")
    #4TH LEVEL
    mbt.insert("H", "....")
    mbt.insert("V", "...-")
    mbt.insert("F", "..-.")
    mbt.insert("", "..--")
    mbt.insert("L", ".-..")
    mbt.insert("", ".-.-")
    mbt.insert("P", ".--.")
    mbt.insert("J", ".---")
    mbt.insert("B", "-...")
    mbt.insert("X", "-..-")
    mbt.insert("C", "-.-.")
    mbt.insert("Y", "-.--")
    mbt.insert("Z", "--..")
    mbt.insert("Q", "--.-")
    mbt.insert("", "---.")
    mbt.insert("", "----")


    mbt.show()