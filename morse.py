class Node:
    #Defining The Node class to default values
    # A Tree has three variables [left, right and a value]

    def __init__(self,value, left=None,right=None):
        self.left = left # left denoting a left child node
        self.right = right # for denoting a right child node
        self.value = value # for denoting a value in a node




letters = "ETIANMSURWDKGOHVF*L*PJBXCYZQ**"
length = len(letters)
COUNT = [2]
getList = []
tree = Node("START")
nexts = []
current = tree
for l in letters.casefold():
    if current.left == None:
        current.left = Node(l)
    else:
        if current.right == None:
            current.right = Node(l)
        else:
            nexts.append(current.left)
            nexts.append(current.right)
            # print(nexts[0].value)
            current = nexts.pop(0)
            current.left = Node(l)
    # print(current.value)
        

def morse_encode(text, root, values):
    if root == None:
        return False
    elif root.value == text:
        return True
    else:
        if morse_encode(text, root.left, values) == True:
            values.insert(0,".")
            root = root.left
            return True
        elif morse_encode(text, root.right, values) == True:
            values.insert(0,"-")
            root = root.right
            return True
        
def encode(text):
    values = []
    for char in text.casefold():
        value = []
        root = tree
        morse_encode(char, root, value)
        values.append("".join(value))

    return " ".join(values)

def decode(text):
    decoded = ""
    # get the whole binary tree starting from the root
    # set as current tree node
    
    encoded_values = text.split(' ')
    # iterate through each character either '.' or '-'
    # if the current character is '.' go through the left node
    # but if it is '-', go through the right node
    
    # return the node value after done decoding
    for encoded in encoded_values:
        node = tree
        for char in encoded:
            if char == '.':
                node = node.left
            else:
                node = node.right
        decoded += node.value
        
    return decoded

def getNode(root, space, let):
    if root == None:
        return
    
    space += COUNT[0]
    for i in range(COUNT[0], space):
        print(end = " ")
    # getList.append(root.value)
    print(let + root.value)
    getNode(root.left, space,let="l - ")
    # process right child
    getNode(root.right, space, let="r - ")

def printTree():

    getNode(tree, 0, "r - ")

            

