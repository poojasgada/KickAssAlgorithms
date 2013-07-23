'''
Created on Jul 17, 2013

@author: psgada
'''
'''
This is a simple Binary Search Tree Library(Sounds cool when i say it as 'Library', Hence :-))

Functions available:
1. Inserting Node in BST
2. Traversals in BST - Inorder, Postorder, Preorder
3. Searching in BST

4. Deleting in BST
'''

'''
Deleting in BST - Nodes with 0,1,2 children
'''

class bst():
    
    class Node():
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
            
    def __init__(self):
        self.root = None
    
    def insert_bst(self, node_i, data):
        if node_i == None:
            node_i = self.Node(data)
            
        else:
            if node_i.data >= data:
                node_i.left = self.insert_bst(node_i.left, data)
            else:
                node_i.right = self.insert_bst(node_i.right, data)
                
        return node_i
    
    def search_bst(self, node, data):
        if node == None:
            return False
        
        if node.data == data:
            return True
        elif data <= node.data:
            return self.search_bst(node.left, data)
        else:
            return self.search_bst(node.right, data)
            
        
    def inorder(self, node):
        if node != None:
            self.inorder(node.left)
            print node.data
            self.inorder(node.right)
    
    def postorder(self, node):
        if node != None:
            self.postorder(node.left)
            self.postorder(node.right)
            print node.data
            
    def preorder(self, node):
        if node != None:
            print node.data
            self.preorder(node.left)
            self.preorder(node.right)
            
def test_bst():
    test = bst()
    
    test.root = test.insert_bst(test.root, 2)
    test.root = test.insert_bst(test.root, 1)
    test.root = test.insert_bst(test.root, 3)
    
    test.inorder(test.root)
    #test.preorder(test.root)
    #test.postorder(test.root)
    
    print test.search_bst(test.root, 3)
    print test.search_bst(test.root, 4)
    
test_bst()