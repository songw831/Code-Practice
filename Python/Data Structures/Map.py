from random import *
class Mapbase(MutableMapping):

    class _Item:

        __slots__ = 'key','value'

        def __init__(self,k,v):
            self._key=k
            self._value=v

        def __eq__(self,other):
            return self._key==other.__key

        def __ne__(self, other):
            return not (self==other)

        def __lt__(self,other):
            return  self._key<other._key




class UnsortedTableMap(Mapbase):

    def __init__(self):
        self._table=[]


    def __getitem__(self, k):

        for item in self._table:
            if k==item._key:
                return item._value

        raise KeyError


    def __setitem__(self,k,v):

        for item in self._table:
            if k==item._key:
                item._value=v
        self._table.append(self._Item(k,v))


    def __delitem__(self, k):
        for j in range(len(self._table)):
            if k==self._table[j]._key:
                self._table.pop(j)
                return
        raise KeyError


    def __len__(self):
        return len(self._table)


    def __iter__(self):
        for item in self._table:
            yield item._key


class HashMapBase(Mapbase):

    def __init__(self,cap=11,p=109345121):
        self._table=cap*[None]
        self._n=0
        self._prime=p
        self._scale=1+randrange(p-1)
        self._shift=randrange(p)


    def _hash_function(self,k):
        return (hash(k)*self._scale+self._shift)%self._prime%len(self._table)


    def __len__(self):
        return self._n

    def __getitem__(self, k):
        j=self._hash_function(k)
        return self._bucket_getitem(j,k)

    def  __setitem__(self, k,v):
        j=self._hash_function(k)
        self._bucket_setitem(j,k,v)
        if self.n>len(self._table)//2:
            self._resize(2*len(self._table)-1)

    def __delitem__(self, k):
        j=self._hash_function(k)
        self._bucket_delitem(j,k)
        self._n-=1

    def _resize(self,c):
        old=list[self.items()]
        self._table=c*[None]
        self._n=0
        for (k,v) in old:
            self._table[k]=v

class  ChainHashMap(HashMapBase):

    def _bucket_getitem(self,j,k):
        bucket=self._table[j]
        if bucket is None:
            raise KeyError
        return bucket[k]


    def _bucket_setitem(self,j,k,v):
        if self._table[j] is None:
          self._table[j]=UnsortedTableMap
        oldsize=len(self._table[j])
        self._table[j][k]=v
        if len(self._table[j])>oldsize:
            self._n+=1


    def _bucket_delitem(self,j,k):
        bucket=self._table[j]
        if bucket is None:
            raise KeyError
        del bucket[k]

    def __iter__(self):
        for bucket in  self._table:
            if bucket is not None:
                for key in bucket:
                    yield key


class ProbeHashMap(HashMapBase):
    _AVAIL=object()

    def _is_available(self,j):
        return self._table[j] is None or self._table[j] is ProbeHashMap._AVAIl


    def _find_slot(self,j,k):
        firstAvail=None
        while True:
            if self._is_available(j):
                if firstAvail is None:
                    firstAvail=j
                if self._table[j] is None:
                    return (False,firstAvail)
            elif k==self._table[j]._key:
                return (True,j)
            j=(j+1)%len(self._table)

    def _bucket_getitem(self,j,k):
        found,s=self._find_slot(j,k)
        if not found:
            raise KeyError
        return self._table[s]._value

    def _bucket_setitem(self,j,k,v):
        found,s=self._find_slot(j,k)
        if not found:
            self._table[s]=self._Item(k,v)
            self._n+=1
        else:
            self._table._value==v

    def _bucket_delitem(self,j,k):
        found,s=self._find_slot(j,k)
        if not found:
            raise KeyError
        self._table[s]=ProbeHashMap._AVAIL



    def __iter__(self):
        for j in range(len(self._table)):
            if not self._is_available(j):
                yield self._table[j]._key



class SortedTableMap(Mapbase):

    def _find_index(self,k,low,high):

        if high<low:
            return high+1
        else:
            mid=(low+high)//2
            if k==self._table[mid]._key:
                return mid
            elif k<self._table[mid]._key:
                return self._find_index(k,low,mid-1)
            else:
                return self._find_index(k,mid+1,high)



    def __init__(self):
        self._table=[]


    def __len__(self):
        return len(self._table)


    def __getitem__(self, k):
        j=self._find_index(k,0,len(self._table)-1)
        if j==len(self._table) or self._table[j]._key!=k:
            raise KeyError
        return self._table[j]._value


    def __setitem__(self, k,v):
        j=self._find_index(k,0,len(self._table)-1)
        if j<len(self._table) and self._table[j]==k:
            self._table[j]._value=v
        else:
            self._table.insert(j,self._item(k,v))



    def __delitem__(self, k):
        j = self._find_index(k, 0, len(self._table) - 1)
        if j==len(self._table) or self._table[j]._key!=k:
            raise KeyError
        self._table.pop(j)



    def __iter__(self):
        for item in self._table:
            yield item._key


    def __reversed__(self):
        for item in reversed(self._table):
            yield  item._key


    def find_min(self):

         if len(self._table)>0:
             return (self._table[0]._key,self._table[0]._value)
         else:
             return None


    def find_max(self):
        if len(self._table)>0:
            return (self._table[-1]._key,self._table[-1]._value)
        else:
            return None

    def find_ge(self,k):
        j=self._find_index(k,0,len(self._table)-1)
        if j<len(self._table):
            return (self._table[j]._key,self._table[j]._value)
        else:
            return None

    def find_lt(self,k):
        j = self._find_index(k, 0, len(self._table) - 1)
        if j>0:
            return (self._table[j-1]._key,self._table[j-1]._value)
        else:
            return None

    def find_range(self,start,stop):
        if start is None:
            j=0
        else:
            j=self._find_index(start,0,len(self._table)-1)
        while j<len(self._table) and (stop is None or self._table[j]._key<stop):
            yield (self._table[j]._key,self._table[j]._value)
            j+=1


    def find_gt(self,k):
        j=self._find_index(k,0,len(self._table)-1)
        if j<len(self._table) and self._table[j]==k:
            j+=1
        if j<len(self._table):
            return (self._table[j]._key,self._table[j]._value)
        else:
            return None

class CostPerformanceDatabase:

    def __init__(self):
        self._M=SortedTableMap

    def best(self,c):
        return self._M.find_le(c)

    def add(self,c,p):

        other=self._M.find_le(c)
        if other is not None and other[1]>=p:
            return
        self._M[c]=p
        other=self._M.find_ge(c)
        while other is not None and other[1]<=p:
            del self._M[other[0]]
            other=self._M.find_ge(c)


class MultiMap:

    _MapType=dict

    def __init__(self):

        self._map=self._MapType()
        self._n=0


    def __iter__(self):
        for k,secondary in self._map.items():
            for v in secondary:
                yield (k,v)


    def add(self,k,v):
        container=self._map.setdefault(k,[])
        container.append(v)
        self._n+=1

    def pop(self,k):
        secondary=self._map[k]
        v=secondary.pop()
        if len(secondary)==0:
            del self._map[k]
        self._n-=1
        return (k,v)

    def find(self,k):
        secondary=self._map[k]
        return (k,secondary[0])

    def find_all(self,k):
        secondary=self._map.get(k,[])
        for v in secondary:
            yield (k,v)







