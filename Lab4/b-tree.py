# Code to implement a B-tree 
# Programmed by Olac Fuentes
# Last modified February 28, 2019

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

def BTreeToSorted(T):
    t = []
    if T.isLeaf:
        return T.item
    else:
        for i in range(len(T.item)):
            t += BTreeToSorted(T.child[i]) + [T.item[i]]
        t += BTreeToSorted(T.child[len(T.item)])
    return t

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

L = []
for i in range(100):
    L[i] = i + 1
    print(L)
# No full nodes
# L = [30, 50, 10, 20, 60, 70, 100, 40, 90, 80, 110, 120, 1, 11 , 3, 4, 5,105, 115, 200, 2, 45, 6]
# Top full node
# L = [30, 50, 10, 20, 60, 70, 100, 40, 90, 80, 110, 120, 1, 11 , 3, 4, 5,105, 115, 200]
# 3 full leaft
# L = [30, 50, 10, 20, 60, 70, 100, 40, 90, 80, 110, 120, 1, 11 , 3, 4, 5,105, 115, 2, 45,46,47]
# L = []
T = BTree()  
for i in L:
    # print('Inserting',i)
    Insert(T,i)
    # PrintD(T,'') 
    # Print(T)
    # print('\n####################################')
    
# SearchAndPrint(T,60)
# SearchAndPrint(T,200)
# SearchAndPrint(T,25)
# SearchAndPrint(T,20)

# Question 1
# print("Question 1")
# print(height(T))

# Question 2
# print("Question 2")
# print(len(L))
# print(len(BTreeToSorted(T)))

# Question 3
# print("Question 3")
# print(MinAtDepth(T,2))

# Question 4
# print("Question 4")
# print(MaxAtDepth(T,2))

# Question 5
# print("Question 5")
# print(NodesAtDepth(T,1))

# Question 6
# print("Question 6")
# PrintAtDepth(T,2)

# Question 7
# print("Question 7")
# print(FullNodes(T))

# Question 8
# print("Question 8")
# print(FullLeafs(T))