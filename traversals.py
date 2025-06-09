# Types of traversal:
#     Pre-order
#     Post-order
#     In-order
class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        
    def insert(self, key, value):
        if key.value < self.value:
            if self.left is None
            self.left = TreeNode(key, value)
            else:
                self.left.insert(key, value)
        else:
            self.right = TreeNode(key, value)
    
    def in_order_traversal(self):
        if self.left:
            self.left.in_order_traversal()
        print (self.value)
            
        if self.right:
            self.right.in_order_traversal()
        
    def pre_order_traversal(self):
         print(self,value)
        if self.left:
            self.left.pre_order_traversal()
            
        if self.right:
            self.right.pre_order_traversal()
                  
    
    def post_order_traversal(self):
        if self.left:
            self.left.post_order_traversal()
            
        if self.right:
            self.right.post_order_traversal()
            
        print(self,value)
        
    def find(self, key):
        if key < self.value:
            
            if self.left is None:
                return False
            else:
                return self.left.find(key)
        
        elif key > self.value:
            if self.right is None:
                return false 
            else: 
                return self.right.find(key)
            
        else: 
            return True
            
        
if name == '__main__':
    trav = TreeNode('A')
    trav.insert(5)
    trav.insert(7)
    trav.insert(11)
    trav.insert(3)
    trav.insert(4)
    trav.insert(8)
    trav.insert(2)
    
    trav.in_order_traversal
    
    
    