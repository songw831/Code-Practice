
def merge(S1,S2,S):

    i=j=0
    while i+j<len(S):
        if (i < len(S1) and S1[i] < S2[j]) or j == len(S):
            S[i+j] = S1[i]
            j += 1
        else:
            S[i+j] = S2[j]
            j += 1


def merge_sort(S):

    n = len(S)
    if n < 2:
        return
    mid = n // 2
    S1 = S[0:mid]
    S2 = S[mid:n]
    merge_sort(S1)
    merge_sort(S2)
    merge(S1,S2,S)

def merge(S1,S2,S):

    while not S1.is_empty() and not S2.is_empty():
        if S1.first() < S2.first():
            S.enqueue(S1.dequeue())

        else:
            S.enqueue(S2.dequeue())

    while not S1.is_empty():
        S.enqueue(S1.dequeue)

    while not S2.is_empty():
        S.enqueue(S2.dequeue())


    def merge_sort(S):

        n = len(S)
        if n < 2:
            return
        S1 = LinkedQueue()
        S2 = LinkedQueue()
        while len(S1) < n // 2:
            S1.enqueue(S.dequeue())
        while  not S.is_empty():
            S2.enqueue(S.dequeue())
        merge_sort(S1)
        merge_sort(S2)
        merge(S1,S2,S)


def quick_sort(S):

    n = len(S)
    if n < 2:
        return

    p=S.first()
    L=LinkedQueue()
    E=LinkedQueue()
    G=LinkedQueue()
    while not S.is_empty:
        if S .first() < p:
            L.enqueue(S.dequeue())
        elif p < S.first():
            G.enqueue(S.dequeue())
        else:
            E.enqueue(S.dequeue())

    quick_sort(L)
    quick_sort(G)

    while not L.is_empty():
        S.enqueue(L.dequeue())

    while not E.is_empty():
        S.enqueue(E.dequeue())

    while not G.is_empty():
        S.enqueue(G.dequeue())



def inplace_quick_sort(S,a,b):

    if a >= b: return
    pivot = S[b]
    left = a
    right = b-1
    while left <= right:
        while left <= right and S[left] < pivot:
            left += 1
        while left <= right and pivot < S[right]:
            right -= 1
        if left <= right:
            S[left],S[right] = S[right],S[left]
            left, right = left + 1, right - 1
        inplace_quick_sort(S,a,left-1)
        inplace_quick_sort(S,left+1,b)




def quick_select(S,k):

    if len(S) == 1:
        return S[0]

    pivot = random.choice(S)

    L = [x for x in S if x < pivot]
    E = [x for x in S if x == pivot]
    G = [x for x in S if x > pivot]

    if k < len(L):
        return quick_select(L,k):
    elif k <= len(L) + len(E)
        return pivot
    else:
        j=k - len(S) - len(E)
        return quick_select(G,j)