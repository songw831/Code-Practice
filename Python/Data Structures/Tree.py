def depth(self,p)
    if self.is_root(p):
        return 0
    else:
        return 1+self.depth(self.parent(p))

def height(self,p):
    if self.is_leaf(p):
        return 0
    else:
        return 1+max(self._height(c) for c in self.chilren(p))

def _add_root(self,e):
    if self._root is not None:raise TypeError
    self._size=1
    self._root=self._Node(e)
    return self._make_position(self._root)

def _add_left(self,p,e):
    node=self._validate(p)
    if node._left is not None:raise TypeError
    self._size+=1
    node._left=self._Node(e,node)
    return self._make_position(node._left)

def _add_right(self,p,e):
    node = self._validate(p)
    if node._right is not None: raise TypeError
    self._size += 1
    node._right= self._Node(e, node)
    return self._make_position(node._right)

def replace(self,p,e):
    node=self._validate(p)
    old=node._element
    node._element=e
    return old

def _delete(self,p):
    node=self._validate(p)
    if self.num_children(p)==2:raise ValueError
    child=node._left if node._left else node._right
    if child is not None:
    child._parent=node._parent
    if self._root==node:
        self._root=child
    else:
        parent=node._parent
        if node is parent._left:
            parent._left=child
        else:
            parent._right=child
    self._size-=1
    node._parent=node
    return node._element

def _attach(self,p,t1,t2):
    node=self._validate(p)
    if not self.is_leaf(p): raise ValueError
    if  not type(self) is type(t1) is type(t2):
        raise ValueError('Tree types must be the same')
    self._size=len(t1)+len(t2)
    if not t1.is_empty:
        t1._root._parent=node
        node._left=t1._root
        t1._root=None
        t1._size=0
    if not t2.is_empty:
        t2._root._parent = node
        node._left = t2._root
        t2._root = None
        t2._size = 0


def preorder(self):
    if not self.is_empty:
        for p in self._subtree_preorder(self._root):
            yield p

def _subtree_preorder(self,p):
    yield p
    if self.chilren(p) is not None:
       for c in self.chilren(p):
         for other in self._subtree_preorder(c):
             yield other

def postorder(self):
    if not self.is_empty:
        for p in self._subtree_postorder(self._root):
            yield p

def _subtree_postorder(self,p):
    if self.chilren(p) is not None:
       for c in self.chilren(p):
          for other in self._subtree_postorder(c):
              yield other
    yield p

def breadthfirst(self):
    if not self.is_empty:
        fringe=LinkedStack()
        fringe.enqueue(self._root)
        while not fringe.is_empty:
            p=fringe.dequeue()
            yield p
            for c in self.children(p):
                fringe.enqueue(c)


