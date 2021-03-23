
def add_first(L,e):
    newest=Node(e)
    newest.next=L.head
    L.head=newest
    L.size+=1

def add_last(L,e):
    newest=Node(e)
    newest.next=None
    L.tail.next=newest
    L.tail=newest
    L.size+=1

def remove_first(L,e):
    if L.head==None:
        raise TypeError
    L.head=L.head.next
    L.size-=1

class LinkedStack:


   class Node:
       __slots__ = '_element','_next'

       def __init__(self,element,next):
         self._element=element
         self._next=next


   def __init__(self):
       self._head=None
       self._size=0

   def __len__(self):
       return self._size

   def is_empty(self):
       return self._size==0

   def push(self,e):
       self._head=self._Node(e,self._head)
       self._size+=1

   def top(self):

       if self.is_empty():
           raise TypeError('Stack is empty')
       return self._head._element

   def pop(self):
       if self.is_empty():
           raise TypeError('Stack is empty')
       answer=self._head._element
       self._head=self._head._next
       self._size-=1
       return answer


class LinkedQueue:


    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next



    def __init__(self):
        self._head=None
        self._tail=None
        self._size=0


    def __len__(self):
        return self._size


    def is_empty(self):
        return self._size==0

    def first(self):

        if self.is_empty():
            raise TypeError('Queue is empty')
        return self._head._element

    def dequeue(self):
        if self.is_empty():
            raise TypeError('Queue is empty')
        answer=self._head._element
        self._head=self._head._next
        self._size-=1
        if self._size==0:
            self._tail=None
        return answer

    def enqueue(self,e):
        newest=self._Node(e,None)
        if self.is_empty():
            self._head=newest
        else:
            self._tail._next=newest
        self._tail=newest
        self._size+=1

class CircularQueue:


    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next



    def __init__(self):
        self._tail=None
        self._size=0


    def __len__(self):
        return self._size


    def is_empty(self):
        return self._size==0

    def first(self):
        if self.is_empty():
            raise TypeError('Queue is empty')
        head=self._tail._next
        return head._element

    def dequeue(self):
        if self.is_empty():
            raise TypeError('Queue is empty')
        oldhead=self._tail._next
        self._tail._next=oldhead._next
        self._size-=1
        return oldhead._element


    def enqueue(self,e):
        newest=CircularQueue._Node(e,None)
        if self.is_empty():
            newest._next=newest
        else:
            newest._next=self._tail._next
            self._tail._next=newest
        self._tail=newest
        self._size+=1


    def rotate(self):
        if self._size>0:
            self._tail=self._tail._next



