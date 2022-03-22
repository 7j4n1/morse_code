class TreeNode:
    def __init__(self, data, left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

class BTree(object):
    def __init__(self):
        self.tnode = None
        self.tnodes = []

    def _create_node(self, data):
        # Create and instantiate a treeNode with supplied data

        n_node = TreeNode("")
        n_node.data = data

        return n_node
    def insert(self, node):
        # insert the new node into the tree at the correct location.
        if self.tnode is None:
            self.tnode = node
        else:
            # create temporary tree
            cursor = self.tnode
            while True:
                if node.data < cursor.data:
                    if cursor.left is None:
                        cursor.left = node
                        # break the loop
                        break
                    else:
                        # let cursor be the left node
                        cursor = cursor.left
                if node.data >= cursor.data:
                    if cursor.right is None:
                        cursor.right = node
                        # break the loop
                        break
                    else:
                        # change cursor to right node leaf or branch
                        cursor = cursor.right

    # function to call to insert data into tree
    def insert_key(self, data):
        new_node = self._create_node(data)
        self.insert(new_node)
