class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None
    
    def insert(self, data):
        node = Node(data)
        
        if self.root == None:
            self.root = node
        else:
            if node.data == self.root.data:
                return
            if node.data > self.root.data:
                rightTree = self.root.right
                while rightTree != None:
                    prev = rightTree
                    
                    if node.data > rightTree.data:
                        if rightTree.right == None:
                            prev.right = rightTree

                    if node.data < rightTree.data:
                        if rightTree.left == None:
                            prev.left = rightTree


tree = BinarySearchTree()
tree.insert(9)