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
    def text_encode(self,data, node, encodeList):
        if node == None:
            return False
        elif node.data == data:
            return True
        else:
            if self.text_encode(data, node.left, encodeList) == True:
                encodeList.insert(0,".")
                node = node.left
                return True
            elif self.text_encode(data, node.right, encodeList) == True:
                encodeList.insert(0,"-")
                node = node.right
                return True
    
    def encode(self, msg: str):
        '''
            Function to Encode provided message and 
            return morse code

            msg: str -> return encoded string
        '''
        encodedList = []
        for letter in msg.upper():
            mlist = []
            self.text_encode(letter, self.root, mlist)
            encodedList.append("".join(mlist))
        # convert the encoded list to string and return it
        return " ".join(encodedList)
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

    # 5TH LEVEL
    mbt.insert("5", ".....")
    mbt.insert("4", "....-")
    mbt.insert("", "...-.")
    mbt.insert("3", "...--")
    mbt.insert("", "..-..")
    mbt.insert("¿", "..-.-")
    mbt.insert("?", "..--.")
    mbt.insert("2", "..---")
    mbt.insert("&", ".-...")
    mbt.insert("", ".-..-")
    mbt.insert("+", ".-.-.")
    mbt.insert("", ".-.--")
    mbt.insert("", ".--..")
    mbt.insert("", ".--.-")
    mbt.insert("", ".---.")
    mbt.insert("1", ".----")
    mbt.insert("6", "-....")
    mbt.insert("=", "-...-")
    mbt.insert("/", "-..-.")
    mbt.insert("", "-..--")
    mbt.insert("", "-.-..")
    mbt.insert("", "-.-.-")
    mbt.insert("(", "-.--.")
    mbt.insert("", "-.---")
    mbt.insert("7", "--...")
    mbt.insert("", "--..-")
    mbt.insert("", "--.-.")
    mbt.insert("", "--.--")
    mbt.insert("8", "---..")
    mbt.insert("", "---.-")
    mbt.insert("9", "----.")
    mbt.insert("0", "-----")

    # 6TH LEVEL
    mbt.insert("", "......")
    mbt.insert("", ".....-")
    mbt.insert("", "....-.")
    mbt.insert("", "....--")
    mbt.insert("", "...-..")
    mbt.insert("", "...-.-")
    mbt.insert("", "...--.")
    mbt.insert("", "...---")
    mbt.insert("", "..-...")
    mbt.insert("", "..-..-")
    mbt.insert("", "..-.-.")
    mbt.insert("", "..-.--")
    mbt.insert("", "..--..")
    mbt.insert("_", "..--.-")
    mbt.insert("", "..---.")
    mbt.insert("", "..----")
    mbt.insert("", ".-....")
    mbt.insert("", ".-...-")
    mbt.insert("\"", ".-..-.")
    mbt.insert("", ".-..--")
    mbt.insert("", ".-.-..")
    mbt.insert(".", ".-.-.-")
    mbt.insert("", ".-.--.")
    mbt.insert("", ".-.---")
    mbt.insert("", ".--...")
    mbt.insert("", ".--..-")
    mbt.insert("", ".--.-.")
    mbt.insert("", ".--.--")
    mbt.insert("", ".---..")
    mbt.insert("", ".---.-")
    mbt.insert("\'", ".----.")
    mbt.insert("", ".-----")
    mbt.insert("", "-.....")
    mbt.insert("-", "-....-")
    mbt.insert("", "-...-.")
    mbt.insert("", "-...--")
    mbt.insert("", "-..-..")
    mbt.insert("", "-..-.-")
    mbt.insert("", "-..--.")
    mbt.insert("", "-..---")
    mbt.insert("", "-.-...")
    mbt.insert("", "-.-..-")
    mbt.insert(";", "-.-.-.")
    mbt.insert("!", "-.-.--")
    mbt.insert("", "-.--..")
    mbt.insert(")", "-.--.-")
    mbt.insert("", "-.---.")
    mbt.insert("", "-.----")
    mbt.insert("", "--....")
    mbt.insert("¡", "--...-")
    mbt.insert("", "--..-.")
    mbt.insert(",", "--..--")
    mbt.insert("", "--.-..")
    mbt.insert("", "--.-.-")
    mbt.insert("", "--.--.")
    mbt.insert("", "--.---")
    mbt.insert(":", "---...")
    mbt.insert("", "---..-")
    mbt.insert("", "---.-.")
    mbt.insert("", "---.--")
    mbt.insert("", "----..")
    mbt.insert("", "----.-")
    mbt.insert("", "-----.")
    mbt.insert("", "------")

    # **************_****\"**.********\'**-********;!*)***¡*,****:****************$
    # 7TH LEVEL

    mbt.show()