import ArrayQueue
#from drawtree import draw_bst

class BinaryTree:
    class Node:
        def __init__(self, x : object, v = None) :
            self.parent = self.left = self.right = None
            self.x = x
            self.v = v

        def set_val(self, x) :
            self.x = x

        def insert_left(self) :
            self.left = BinaryTree.Node('') 
            self.left.parent = self
            return self.left

        def insert_right(self) :
            self.right = BinaryTree.Node('')
            self.right.parent = self
            return self.right

    def __init__(self) : 
        self.r = None
        self.nil = None

    def depth(self, u : Node) -> int:
        d = 0
        while u is not self.r:
            u = u.parent
            d += 1

    def size(self) -> int:
        return self._size(self.r)
    
    def _size(self, u : Node) -> int:
        if u == self.nil: return 0
        return 1 + self._size(u.left) + self._size(u.right)
    
    def size2(self) -> int:
        u = self.r
        prv = None
        n = 0
        while u is not None:
            if prv == u.parent:
                n += 1
                if u.left is not None:
                    nxt = u.left
                elif u.right is not None:
                    nxt = u.right
                else:
                    nxt = u.parent
            elif prv == u.left:
                if u.right is not None:
                    nxt = u.right
                else:
                    nxt = u.parent
            else:
                nxt = u.parent
            prv = u
            u = nxt
        return n

    def height(self) -> int:
        return self._height(self.r)
    
    def _height(self, u : Node) -> int:
        if u == self.nil: return 0
        return 1 + max(self._height(u.left), self._height(u.right))
    
    def traverse(self, u : Node):
        if u is None:
            return
        self.traverse(u.left)
        self.traverse(u.right)

    def traverse2(self):
        u = self.r
        prv = None
        while u is not None:
            if prv == u.parent:
                if u.left is not None:
                    nxt = u.left
                elif u.right is not None:
                    nxt = u.right
            elif prv == u.left:
                if u.right is not None:
                    nxt = u.right
                else:
                    nxt = u.parent
            else:
                nxt = u.parent
            prv = u
            u = nxt

    def bf_traverse(self):
        q = ArrayQueue.ArrayQueue()
        l = []
        if self.r is not None:
            q.add(self.r)
            l.append(self.r.v)
            while q.size() > 0:
                u = q.remove()
                if u.left is not None:
                    q.add(u.left)
                    l.append(u.left.v)
                if u.right is not None:
                    q.add(u.right)
                    l.append(u.right.v)
        return l
            
    def first_node(self):
        w = self.r
        if w == self.nil: return self.nil
        while w.left != self.nil:
            w = w.left
        return w
    
    def next_node(self, w):
        if w.right != self.nil:
            w = w.right
            while w.left != self.nil:
                w = w.left
        else:
            while w.parent != self.nil and w.parent.left != w:
                w = w.parent
            w = w.parent
        return w
    
    def in_order(self) :
        if self.r is not self.nil:
            self.__in_order(self.r)

    def pre_order(self) :
        if self.r is not self.nil:
            self.__pre_order(self.r)

    def pos_order(self) :
        if self.r is not self.nil:
            self.__pos_order(self.r)

    def __in_order(self, u : Node) :
        if u.left is not self.nil:
            self.__in_order(u.left)
        print(f"{u.x}: {u.v}")
        if u.right is not self.nil:
            self.__in_order(u.right)

    def __pre_order(self, u : Node) :
        print(f"{u.x}: {u.v}")
        if u.left is not self.nil:
            self.__pre_order(u.left)
        if u.right is not self.nil:
            self.__pre_order(u.right)

    def __pos_order(self, u : Node) :
        if u.left is not self.nil:
            self.__pos_order(u.left)
        if u.right is not self.nil:
            self.__pos_order(u.right)
        print(f"{u.x}: {u.v}")

    def __str__(self):
        l = []
        #self.in_order(self.r, l)
        return ', '.join(map(str, l))