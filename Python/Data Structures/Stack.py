class ArrayStack:

    def __init__(self):
        self._data=[]

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data)==0

    def push(self,e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise TypeError('Stack is empty')
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise TypeError('Stack is empty')
        return self._data.pop()



def is_matched(expr):
    lefty='({['
    righty=')}]'
    S=ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c)
        elif c in righty:
            if S.is_empty():
                return False
            if righty.index(c)!=lefty.index(S.pop()):
                return False
    return S.is_empty()


class ArrayQueue:
    DEFAULT_CAPACITY=10

    def __init__(self):
        self._data=[None]*ArrayQueue.DEFAULT_CAPACITY
        self._size=0
        self._front=0

    def __len__(self):
        return self._size


    def is_empty(self):
        return self._size==0

    def first(self):
        if self.is_empty():
            raise TypeError('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise TypeError('Queue is empty')
        answer=self._data[self._front]
        self._data[self._front]=None
        self._front=(self._front+1)%len(self._data)
        self._size-=1
        return answer

    def enqueue(self,e):
        if self._size==len(self._data)
            self._resize(2*len(self._data))
        avail=(self._front+self._size)%len(self._data)
        self._data[avail]=e
        self._size+=1


    def _resize(self,cap):
        old=self._data
        self._data=[None]*cap
        walk=self._front
        for i in range(self._size):
            self._data[i]=old[walk]
            walk=(walk+1)%len(old)
        self._front=0

