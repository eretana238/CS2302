class Node(object):

    def __init__(self, item, next=None):

        self.item = item

        self.next = next

class List(object):

    def __init__(self):

        self.head = None

        self.tail = None

def Print(L):

    temp = L.head

    while temp is not None:

        print(temp.item, end=' ')

        temp = temp.next

    print()

def Append(L,x):     

    if IsEmpty(L):

        L.head = Node(x)

        L.tail = L.head

    else:

        L.tail.next = Node(x)

        L.tail = L.tail.next

def IsEmpty(L): 
    return L.head == None

L = List()

for i in range(5):

    Append(L,i)

#Question 3
def Larger(L,n):
    if L != None:
        temp = L.head
        while temp != None:
            
            temp = temp.next
        

#Question 1
def IndexOf(A,n,length):
    i = len(A)-1-length
    if n == A[i]:
        return i
    
    IndexOf(A[1:],n,length-1)

    
    
A = [2,4,6,8]
print(IndexOf(A,4,len(A)-1))