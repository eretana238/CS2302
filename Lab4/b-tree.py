# Course: 2302-001
# Author: Esteban Retana
# Assignment: 
# Instructor: Olac Fuentes
# TA: Anindita Nath
# Date of last modification:3/27/19
# Purpose: 

class BTree(object):
    # Constructor
    def __init__(self,item=[],child=[],isLeaf=True,max_items=5):  
        self.item = item
        self.child = child
        self.isLeaf = isLeaf
        if max_items <3: #max_items must be odd and greater or equal to 3
            max_items = 3
        if max_items%2 == 0: #max_items must be odd and greater or equal to 3
            max_items +=1
        self.max_items = max_items

def FindChild(T,k):
    # Determines value of c, such that k must be in subtree T.child[c], if k is in the BTree    
    for i in range(len(T.item)):
        if k < T.item[i]:
            return i
    return len(T.item)
             
def InsertInternal(T,i):
    # T cannot be Full
    if T.isLeaf:
        InsertLeaf(T,i)
    else:
        k = FindChild(T,i)   
        if IsFull(T.child[k]):
            m, l, r = Split(T.child[k])
            T.item.insert(k,m) 
            T.child[k] = l
            T.child.insert(k+1,r) 
            k = FindChild(T,i)  
        InsertInternal(T.child[k],i)   
            
def Split(T):
    #print('Splitting')
    #PrintNode(T)
    mid = T.max_items//2
    if T.isLeaf:
        leftChild = BTree(T.item[:mid]) 
        rightChild = BTree(T.item[mid+1:]) 
    else:
        leftChild = BTree(T.item[:mid],T.child[:mid+1],T.isLeaf) 
        rightChild = BTree(T.item[mid+1:],T.child[mid+1:],T.isLeaf) 
    return T.item[mid], leftChild,  rightChild   
      
def InsertLeaf(T,i):
    T.item.append(i)  
    T.item.sort()

def IsFull(T):
    return len(T.item) >= T.max_items

def Insert(T,i):
    if not IsFull(T):
        InsertInternal(T,i)
    else:
        m, l, r = Split(T)
        T.item =[m]
        T.child = [l,r]
        T.isLeaf = False
        k = FindChild(T,i)  
        InsertInternal(T.child[k],i)   
        
        
def height(T):
    if T.isLeaf:
        return 0
    return 1 + height(T.child[0])
        

def Search(T,k):
    # Returns node where k is, or None if k is not in the tree
    if k in T.item:
        return T
    if T.isLeaf:
        return None
    return Search(T.child[FindChild(T,k)],k)
                  
def Print(T):
    # Prints items in tree in ascending order
    if T.isLeaf:
        for t in T.item:
            print(t,end=' ')
    else:
        for i in range(len(T.item)):
            Print(T.child[i])
            print(T.item[i],end=' ')
        Print(T.child[len(T.item)])    
 
def PrintD(T,space):
    # Prints items and structure of B-tree
    if T.isLeaf:
        for i in range(len(T.item)-1,-1,-1):
            print(space,T.item[i])
    else:
        PrintD(T.child[len(T.item)],space+'   ')  
        for i in range(len(T.item)-1,-1,-1):
            print(space,T.item[i])
            PrintD(T.child[i],space+'   ')
    
def SearchAndPrint(T,k):
    node = Search(T,k)
    if node is None:
        print(k,'not found')
    else:
        print(k,'found',end=' ')
        print('node contents:',node.item)

# Converts BTree to sorted array list
def BTreeToSorted(T):
    if T == None:
        return
    t = []
    if T.isLeaf:
        return T.item
    else:
        for i in range(len(T.item)):
            t += BTreeToSorted(T.child[i]) + [T.item[i]]
        t += BTreeToSorted(T.child[len(T.item)])
    return t
# Finds out the minimum node at a depth level
def MinAtDepth(T,k):
    # Find out if given depth is possible to search
    h = height(T)
    if k > h:
        return -1
    # Returns smallest item in depth
    if k == 0:
        return T.item[0]
    else:
        return MinAtDepth(T.child[0],k-1)

# Finds out the max value from a certain depth level
def MaxAtDepth(T,k):
    # Find out if given depth is possible to search
    h = height(T)
    if k > h:
        return -1
    # Returns largest item in depth
    if k == 0:
        return T.item[len(T.item)-1]
    else:
        return MaxAtDepth(T.child[len(T.item)],k-1)

# Determiness the amount of nodes at a depth level
def NodesAtDepth(T,k):
    t = 0
    # Find out if given depth is possible to search
    h = height(T)
    if k > h:
        return -1
    # Stop at one depth before the given value to sum the lengths of all childs
    if k >= 1:
        for i in range(len(T.item)):
            t += NodesAtDepth(T.child[i], k-1)
        t += NodesAtDepth(T.child[len(T.item)],k-1)
    # Returns the length of node
    if k == 0:
        return len(T.item)

    return t

# Prints all nodes values at a certain depth level
def PrintAtDepth(T,k):
    h = height(T)
    if k > h:
        return
    if k >= 1:
        for i in range(len(T.item)):
            PrintAtDepth(T.child[i],k-1)

        PrintAtDepth(T.child[len(T.item)],k-1)
    if k == 0:
        for i in range(len(T.item)):
            print(T.item[i], end=' ')

# Finds out the total number of full nodes
def FullNodes(T):
    t = 0
    if T.max_items == len(T.item):
        return 1
    if T.isLeaf:
        return 0
    else:
        for i in range(len(T.item)):
            t += FullNodes(T.child[i])
        t += FullNodes(T.child[len(T.item)])
    return t

# Finds out the toal number of full leaf nodes
def FullLeafs(T):
    t = 0
    if T.isLeaf:
        if T.max_items == len(T.item):
            return 1
    else:
        for i in range(len(T.item)):
            t += FullLeafs(T.child[i])
        t += FullLeafs(T.child[len(T.item)])
    
    return t

# def FindDepth(T,k):
#     if 

# L = []
# for i in range(100):
#     L[i] = i + 1
#     print(L)


# No full nodes
M = [30, 50, 10, 20, 60, 70]
# Top full node
N = [30, 50, 10, 20, 60, 70, 100, 40, 90, 80, 110, 120, 1, 11 , 3, 4, 5,105, 115, 200]
# full leaft
O = [30, 50, 10, 20, 60, 70, 100, 40, 90, 80, 110, 120, 1, 11 , 3, 4, 5, 105, 109, 115, 2, 45, 46, 47]

T = BTree([])

U = BTree()

V = BTree()

W = BTree()

# for i in L:
#     Insert(T,i)

for i in M:
    # print('Inserting',i)
    Insert(U,i)
    # PrintD(W,'') 
    # Print(T)
    # print('\n####################################')

for i in N:
    # print('Inserting',i)
    Insert(V,i)
    # PrintD(W,'') 
    # Print(T)
    # print('\n####################################')

for i in O:
    # print('Inserting',i)
    Insert(W,i)
    # PrintD(W,'') 
    # Print(T)
    # print('\n####################################')
    

# SearchAndPrint(T,60)
# SearchAndPrint(T,200)
# SearchAndPrint(T,25)
# SearchAndPrint(T,20)

# Question 1
print("Question 1")
print(height(T))
print(height(U))
print(height(V))
print(height(W))

# Question 2
print("Question 2")
print(BTreeToSorted(T))
print(BTreeToSorted(U))
print(BTreeToSorted(V))
print(BTreeToSorted(W))

# Question 3
print("Question 3")
print(MinAtDepth(T,1))
print(MinAtDepth(U,1))
print(MinAtDepth(V,2))
print(MinAtDepth(W,2))

# Question 4
print("Question 4")
print(MaxAtDepth(T,1))
print(MaxAtDepth(U,1))
print(MaxAtDepth(V,2))
print(MaxAtDepth(W,2))

# Question 5
print("Question 5")
print(NodesAtDepth(T,1))
print(NodesAtDepth(U,1))
print(NodesAtDepth(V,2))
print(NodesAtDepth(W,2))

# Question 6
print("Question 6")
PrintAtDepth(T,1)
print()
PrintAtDepth(U,1)
print()
PrintAtDepth(V,2)
print()
PrintAtDepth(W,2)
print()

# Question 7
print("Question 7")
print(FullNodes(T))
print(FullNodes(U))
print(FullNodes(V))
print(FullNodes(W))

# Question 8
print("Question 8")
print(FullLeafs(T))
print(FullLeafs(U))
print(FullLeafs(V))
print(FullLeafs(W))

# Question 9
# print("Question 9")