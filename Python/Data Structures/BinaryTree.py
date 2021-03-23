class TreeMap(LinkedBinaryTree,MapBase):
    class Position(LinkedBinary Tree.Position):
        def key(self):
            return self._element()._key

        def value(self):
            return self._element()._value


    def _subtree_search(self,p,k):

        if k==p.key():
            return p
        elif k<p.key():
            if self._left(p) is not None:
                return self._subtree_search(self.left(p),k)
        else:
            if self._right(p) is not None:
                return self._subtree_search(self.right(p),k)

        return p

    def _subtree_first_position(self,p):
        walk = p
        while self.left(walk) is not None:
            walk = self.left(walk)
        return walk

    def _subtree_last_position(self,p):
        walk = p
        while self.left(walk) is not None:
            walk=self.right(walk)
        return walk

    def first(self):
        return self._subtree_first_position(self.root()) if len(self) > 0 else None

    def last(self):
        return self._subtree_last_position(self.root()) if len(self) > 0 else None

    def before(self,p):

        self._validate(p)
        if self.left(p):
            return self._subtree_last_position(self.left(p))
        else:
            walk=p
            above=self.parent(walk)
            while above is not None and walk==self.left(above):
                walk=above
            return above


    def after(self,p):


        self._validate(p)
        if self.right(p):
            walk=self.right(p)
            while self.left(walk) is not None:
                walk=self.left(walk)
            return walk
        else:
            walk=p
            above= self.parent(walk)
            while above is not None and walk == self.right(above):
                walk=above
                above= self.parent
            return above



    def find_position(self,k):

        if self.is_empty():
            return None

        else:
            p=self._subtree_search(self.root(),k)
            self._rebalance_access(p)
            return p


    def find_ge(self,k):

        if self.is_empty():
            return None

        else:
            p=self.find_position(k)
            if p.key() < k:
                p=self.after(p)
            return (p.key(),p.value()) if p is not None else None


    def find_min(self):

        if self.is_empty():
            return None

        else:
            p=self.first()
            return (p.key(),p.value())


    def find_range(self,start,stop):

        if not self.is_empty():
            if start is None:
                p=self.first()

            else:

                p=self._find_position(start)
                if p.key()<start:
                    p=self.after(p)
            while p is not None and (stop is None or p.key()<stop):
                yield (p.key(),p.value())
                p=self.after(p)


    def __getitem__(self, k):

         if self.is_empty():
             raise KeyError

         else:
             p=self._subtree_search(self.root(),k)
             self._reblannce_access(p)
             if k != p.key():
                 raise KeyError
             return p.value()



    def __setitem__(self, k, v):

        if self.is_empty():
            leaf=self._add_root(self._Item(k,v))

        else:
            p=self._subtree_search(self.root(),k)
            if p.key() == k:
                p.element()._value=v
                self._rebalance_accesss(p)
                return

            else:
                item=self._Item(k,v)
                if p.key()<k:
                    leaf=self._add_right(p,item)
                else:
                    leaf=self._add_left(p,item)
            self._rebalance_insert(leaf)


    def  __iter__(self):

        p=self.first()
        while p is not None:
            yield p.key()
            p = self.after(p)



    def  delete(self,p):

        self._validate(p)
        if self.left(p) and self.right(p):
            replacement=self._subtree_last_position(self.left(p))
            self._replace(p,replacement.element())
            p = replacement
        parent = self.parent(p)
        self._delete(p)
        self._rebalance_delete(parent)


    def __delitem__(self,k):

        if not self.is_empty():
            p=self._subtree_search(self.root(),k)
            if k == p.key():
                self.delete(p)
                return
            self._rebalance_access(p)
        raise KeyError



    def _relink(self,parent,child,make_left_child):

        if make_left_child:
            parent._left=child

        else:
            parent._left=child

            if child is not None:
                child._parent=parent


    def _rotate(self,p):

        x=p._node
        y=x._parent
        z=y._parent

        if z is None:
            self._root=x
            x._parent=None
        else:
            self._relink(z,x,y==z._left)

        if x == y._left:
            self._relink(y,x._right,True)
            self._relink(x,y,False)

        else:
            self._relink(y,x._left,False)
            self._relink(x,y,True)



    def _restructure(self,x):

        y = self.parent(x)
        z = self.parent(y)
        if (x == self.right(y)) == (y == self._right(z)):
            self._rotate(y)
            return y
        else:
            self._rotate(x)
            self._rotate(x)
            return x





class AVLTreeMap(TreeMap):

    class _Node(TreeMap._Node):
         __slots__ = 'height'


       def __init__(self,element,parent=None,left=None,right=None):

           super().__init__(element,parent,left,right)
           self._height=0

       def left_height(self):

           return self._left_height if self._left is not None else 0

       def right_height(self):

            return self._right._height if self._right is not None else 0

    def _recompute_height(self,p):

        p._node._height = 1 + max(p._node.left_height(), p._node.right_height())


    def _isbalanced(self,p):

        return abs(p._node.left_height()-p._node.right_height()) <= 1

    def _tall_child(self,p,favorleft=False):
        if p._node.left_height() + (1 if favorleft else 0):
            return  self.left(p)
        else:
            return self.right(p)


    def _tall_grandchild(self,p):

        child = self._tall_child(p)
        alignment=(child == self.left(p))
        return self._tall_child(child,alignment)


    def _rebalance(self,p):
        while p is not None:
            old_height=p._node._height
            if not self._isbalanced(p):
                p=self._restructure(self._tall_child(p))
                self._recompute_height(self.left(p))
                self._recompute_height(self.right(p))
            self._recompute_height(p)
            if p._node._height == old_height:
                p=None
            else:
                p=self.parent(p)


    def _rebalance_insert(self,p):
        self._rebalance(p)


    def _rebalance_delete(self,p):
        self._rebalance(p)



class SplayTreeMap(TreeMap):

    def _splay(self,p):

        while p != self.root():
            parent = self.parent(p)
            grand = self.parent(parent)
            if grand is None:
                self._rotate(p)
            elif (parent==self.left(grand)) == (p == self.left(parent)):
                self._rotate(parent)
                self._rotate(p)
            else:
                self._rotate(p)
                self._rotate(p)


    def _rebalance_insert(self,p):
        if p is not None:
           self._splay(p)


    def _rebalance_delete(self,p):
        self._splay(p)

    def _rebalance_access(self,p):
        self._splay(p)


class RedBlackTreeMap(TreeMap):

    class _Node(TreeMap._Node):

        __slots__='_red'

       def __init__(self,element,parent=None,left=None,right=None):
          super().__init__(element,parent,left,right)
          self._red=True

       def _set_red(self,p): p._node._red=True
       def _set_black(self,p):p._node._red=False
       def _set_color(self,p,make_red):p._node._red=make_red
       def _is_red(self,p):return p is not None and p._node._red
       def is_red_leaf(self,p):return self._is_red(p) and self.is_leaf(p)


       def _get_red_child(self,p):
          for child in (self.left(p),self.right(p)):
              if self.is_red(child):
                  return child
          return None



       def _rebalance_insert(self,p):
           self._resolve_red(p)

       def _resolve_red(self,p):
           if self.is_root(p):
               self._set_black(p)
           else:
               parent = self.parent(p)
               if self._is_red(parent):
                   uncle = self.sibilig(parent)
                   if not self._is_red(uncle):
                       middle = self._restructure(p)
                       self._set_black(middle)
                       self._set_red(self.left(middle))
                       self._set_red(self.right(middle))
                   else:
                       grand = self.parent(parent)
                       self._set_red(grand)
                       self._set_black(self.left(grand))
                       self._set_black(self.right(grand))
                       self._resolve_red(grand)



