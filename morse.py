class Node:
    #Defining The Node class to default values
    # A Tree has three variables [left, right and a value]

    def __init__(self,value, left=None,right=None):
        self.left = left # left denoting a left child node
        self.right = right # for denoting a right child node
        self.value = value # for denoting a value in a node


# find a key
def find(currentNode, key):
    if currentNode is None:
        return False
    else:
        cursor = currentNode
        while True:
            if key < cursor.value:
                if cursor.value == key:
                    return True
                if cursor.left is None:
                    return False
                else:
                    cursor = cursor.left
            if key >= cursor.value:
                if cursor.value == key:
                    return True
                if cursor.right is None:
                    return False
                else:
                    cursor = cursor.right
    


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

'''
 Function to get minimum value node from Binary Tree
 node - TreeNode

 return Node
'''

def minValueNode(node):
    current = node

    while (current.left is not None):
        current = current.left
    return current
'''
 Function to delete node from Binary Tree
 root - TreeNode
 key - value to be deleted from the TreeNode

 return Node
'''
def delete(root, key):
    if root is None:
        return root
    
    if key < root.value:
        root.left = delete(root.left, key)
    elif key > root.value:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        
        temp = minValueNode(root.right)
        root.value = temp.value

        root.right = delete(root.right, temp.value)
    
    return root

# The keys to be insert into nodes tree
# where the * character denotes empty node key
letters = "ETIANMSURWDKGOHVF*L*PJBXCYZQ**54*3*¿?2&*+****16=/***(*7***8*90**************_****\"**.********\'**-********;!*)***¡*,****:****************$"
COUNT = [2]
# Initiate a root node with key (START)
MorseTree = Node("START")
nexts = []
# instantiate the current MorseTree
node = MorseTree
# iterating the keys and inserting it into the binary MorseTree
for l in letters.casefold():
    
    if node.left == None:
        node.left = Node(l)
    else:
        if node.right == None:
            node.right = Node(l)
        else:
            nexts.append(node.left)
            nexts.append(node.right)
            node = nexts.pop(0)
            node.left = Node(l)
        

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
        
def encode(text):
    values = []
    for char in text.casefold():
        value = []
        root = MorseTree
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
        node = MorseTree
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
    print(root.value)
    # process the left child(s)
    getTree(root.left, space,let="l - ")
    # process right child(s)
    getTree(root.right, space, let="r - ")

# function to print Binary Tree Stack
def printTree():
    # call the get Node function to print each node
    # and set the root node first.
    getTree(MorseTree)

def delete_key(key):
    delete(MorseTree,key)
# def main():
#     g = nodes

# print the Morse Binary Tree if called directly
if __name__ == '__main__':
    # printTree()
    # delete(MorseTree, "T")
    # printTree()
    text = encode('usdt')
    print(text)


