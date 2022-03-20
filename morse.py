class Node:
    #Defining The Node class to default values
    # A Tree has three variables [left, right and a value]

    def __init__(self,value, left=None,right=None):
        self.left = left # left denoting a left child node
        self.right = right # for denoting a right child node
        self.value = value # for denoting a value in a node


class morse:
    def __init__(self):
        self.letters = "ETIANMSURWDKGOHVF*L*PJBXCYZQ**"
        self.tree = Node("START")
        nexts = []
        self.current = self.tree
        for l in self.letters:
            if self.current.left == None:
                self.current.left = Node(l)
            else:
                if self.current.right == None:
                    self.current.right = Node(l)
                else:
                    nexts.append(self.current.left)
                    nexts.append(self.current.right)
                    # print(nexts[0].value)
                    self.current = nexts.pop(0)
                    self.current.left = Node(l)
            # print(self.current.value)
        

    def morse_encode(self, text, root, values):
        if root == None:
            return False
        elif root.value == text:
            # print(self.encoded)
            return True
        else:
            if self.morse_encode(text, root.left, values) == True:
                values.insert(0,".")
                root = root.left
                return True
            elif self.morse_encode(text, root.right, values) == True:
                values.insert(0,"-")
                root = root.right
                return True
        
    def encode(self, text):
        values = []
        for char in text:
            value = []
            root = self.tree
            # gg = comp_tree.decode("..- ...")
            self.morse_encode(char, root, value)
            values.append("".join(value))

        return " ".join(values)

    
    def decode(self, text):
        self.decoded = ""
        # get the whole binary tree starting from the root
        # set as current tree node
        
        self.encoded_values = text.split(' ')
        # iterate through each character either '.' or '-'
        # if the current character is '.' go through the left node
        # but if it is '-', go through the right node
        
        # return the node value after done decoding
        for encoded in self.encoded_values:
            self.node = self.tree
            for char in encoded:
                if char == '.':
                    self.node = self.node.left
                else:
                    self.node = self.node.right
            self.decoded += self.node.value
            
        return self.decoded
