class Node:
    #Defining The Node class to default values
    # A Tree has three variables [left, right and a value]

    def __init__(self,value, left=None,right=None):
        self.left = left # left denoting a left child node
        self.right = right # for denoting a right child node
        self.value = value # for denoting a value in a node

'''
    Function to insert key into a tree
'''
def insert_node(root, key,lists=[]):
    
    if root == None:
        root = Node(key)
        return root
    else:
        if root.left == None:
            root.left = Node(key)
            return root
        else:
            if root.right == None:
                root.right = Node(key)
            else:
                lists.append(root.left)
                lists.append(root.right)
                root = lists.pop(0)
                root.left = Node(key)
            return root

# The keys to be insert into nodes tree
# where the * character denotes empty node key
letters = "ETIANMSURWDKGOHVF*L*PJBXCYZQ**54*3*¿?2&*+****16=/***(*7***8*90"
COUNT = [2]
# Initiate a root node with key (START)
tree = Node("START")
# nexts = []
# instantiate the current tree
current = tree
# iterating the keys and inserting it into the binary tree
for l in letters.casefold():
    current = insert_node(current, l)

# add 6th & 7th level nodes
sixlevel = "*"*13
sixlevel += "_****\"**.********\'**-********;!*)***¡*,****:*******"
sevlevel = sixlevel + "*********$"

# iterate through the sixth and seventh key and add it to the Tree
for c in sevlevel:
    current = insert_node(current, c)

'''
    Recursive function to encode text
        text - str | character(s) to encode
        root - Node | Binary tree Node
        values - 
'''
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
'''
    Decoding function which calls the recursive morse_encode function
    and then concatenate the string
'''
def encode(text):

    values = []
    for char in text.casefold():
        value = []
        root = tree
        morse_encode(char, root, value)
        values.append("".join(value))

    return " ".join(values)

'''
    Function to decode string text
    text - str | text to decode
'''
def decode(text):
    decoded = ""
    # get the whole binary tree starting from the root
    # set as current tree node
    
    # split the string if it is more than one character
    encoded_values = text.split(' ')
    # iterate through each character either '.' or '-'
    # if the current character is '.' go through the left node
    # but if it is '-', go through the right node
    
    
    for encoded in encoded_values:
        node = tree
        for char in encoded:
            if char == '.':
                node = node.left
            else:
                node = node.right
        decoded += node.value
    # return the decoded string
    return decoded
'''
    Get and print each node from the tree
    with the arguments of three variables
    root - binary tree Nodes
    space - initial root should be 0 which indicate the spacing unit
    let - letter to denote the root node (r - )
'''
def getNode(root, space, let):
    if root == None:
        return
    
    space += COUNT[0]
    for i in range(COUNT[0], space):
        print(end = " ")
    print(let + root.value)
    # process the left child(s)
    getNode(root.left, space,let="l - ")
    # process right child(s)
    getNode(root.right, space, let="r - ")

# function to print Binary Tree Stack
def printTree():
    # call the get Node function to print each node
    # and set the root node first.
    getNode(tree, 0, "r - ")



# print the Morse Binary Tree if called directly
if __name__ == '__main__':
    printTree()  
    # g = Node(2)
    # insert_node(g,6)

