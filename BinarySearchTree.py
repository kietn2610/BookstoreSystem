from BinaryTree import BinaryTree
from Interfaces import Set


class BinarySearchTree(BinaryTree, Set):

    def __init__(self, nil=None):
        super().__init__()
        self.n = 0
        self.nil = nil
        
    def clear(self):
        self.r = self.nil
        self.n = 0

    def new_node(self, x):
        u = BinaryTree.Node(x)
        u.left = u.right = u.parent = self.nil
        return u
    
        
    def find_last(self, x : object) -> BinaryTree.Node:     #edit
        w = self.r
        prev = None
        while w != None:
            prev = w
            if x < w.x:
                w = w.left
            elif x > w.x:
                w = w.right
            else:
                return w
        return prev
        
    def add_child(self, p : BinaryTree.Node, u : BinaryTree.Node) -> bool:  #edit
        if p == None:
            self.r = u
        else:
            if u.x < p.x:
                p.left = u
            elif u.x > p.x:
                p.right = u
            else:
                return False
            u.parent = p
        self.n += 1
        return True

    def find_eq(self, x : object) -> object:    #edit
        w = self.r
        while w != None:
            if x < w.x:
                w = w.left
            elif x > w.x:
                w = w.right
            else:
                return w
        return None
    
    def find(self, x: object) -> object:    #edit
        w = self.r
        z = None
        while w != None:
            if x < w.x:
                z = w
                w = w.left
            elif x > w.x:
                w = w.right
            else:
                return w.v
        if z == None:
            return None
        return z.v
        
    def add(self, key : object, value : object) -> bool:    # edit
        p = self.find_last(key)
        return self.add_child(p, BinaryTree.Node(key, value))
        
    def add_node(self, u : BinaryTree.Node) -> bool: # edit
        p = self.find_last(u.x)
        return self.add_child(p, u)
    
    def splice(self, u: BinaryTree.Node):   # edit
        if u.left != None:
            s = u.left
        else:
            s = u.right
        if u == self.r:
            self.r = s
            p = None
        else:
            p = u.parent
            if p.left == u:
                p.left = s
            else:
                p.right = s
        if s != None:
            s.parent = p
        self.n -= 1

    def remove_node(self, u : BinaryTree.Node): # edit
        if u.left == None or u.right == None:
            self.splice(u)
        else:
            w = u.right
            while w.left != None:
                w = w.left
            u.x = w.x
            self.splice(w)

    def remove(self, x : object) -> bool:   # edit
        try:
            w = self.find_eq(x)
            self.remove_node(w)
        except Exception:
            print(f'Invalid removal, received {w}...')
             
    def __iter__(self):
        u = self.first_node()
        while u != self.nil:
            yield u.x
            u = self.next_node(u)


'''
q = BinarySearchTree()
q.add(3, "third")
q.add(2, "second")
q.add(1, "first")
print(q.find(2.5))
q.remove(3)
print(q.find(3))
q.add(3, "third")
q.add(5, "fifth")
q.add(4, "fourth")
print(q.find_eq(3.4))
print(q.find(3.4))
print("In order")
q.in_order()
print("Pre oder")
q.pre_order()
print("Pos order")
q.pos_order()
'''