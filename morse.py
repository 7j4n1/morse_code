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
        return Node(key)
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
# function to check if a root is having a successor node
def successor(root):
    # check the right node
    root = root.right
    # check all the left child nodes
    while root.left:
        root = root.left
    # return root node value
    return root.value
def predecessor(root):
    # check the left node
    root = root.left
    # check all the right child nodes
    while root.right:
        root = root.right
    # return root node value
    return root.value

'''
 Function to delete node from Binary Tree
 root - TreeNode
 key - value to be deleted from the TreeNode

 return Node
'''
def delete_node(root, key):
    if not root:
        return None
    
    if not (root.left or root.right):
        root = None
    elif root.right:
        root.value = successor(root)
        root.right = delete_node(root.right, root.value)
    else:
        root.value = predecessor(root)
        root.left = delete_node(root.left, root.value)

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
def getTree(root, space=0, let="r - "):
    if root == None:
        return
    
    space += COUNT[0]
    for i in range(COUNT[0], space):
        print(end = " ")
    print(let + root.value)
    # process the left child(s)
    getTree(root.left, space,let="l - ")
    # process right child(s)
    getTree(root.right, space, let="r - ")

# function to print Binary Tree Stack
def printTree():
    # call the get Node function to print each node
    # and set the root node first.
    getTree(tree)



# print the Morse Binary Tree if called directly
if __name__ == '__main__':
    printTree()  
    # g = Node(2)
    # insert_node(g,6)

