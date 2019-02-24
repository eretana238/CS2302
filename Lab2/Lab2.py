# Course: 2302-001
# Author: Esteban Retana
# Assignment: Practice sorting algorithms
# Instructor: Olac Fuentes
# TA: Anindita Nath
# Date of last modification:2/23/19
# Purpose: Sort linked lists with different sorting algorithms and figure out their time complexity

import random

#Node Functions
class Node(object):
    # Constructor
    def __init__(self, item, next=None):  
        self.item = item
        self.next = next 
        
def PrintNodes(N):
    if N != None:
        print(N.item, end=' ')
        PrintNodes(N.next)
        
def PrintNodesReverse(N):
    if N != None:
        PrintNodesReverse(N.next)
        print(N.item, end=' ')
        
#List Functions
class List(object):   
    # Constructor
    def __init__(self): 
        self.head = None
        self.tail = None
        
def IsEmpty(L):  
    return L.head == None     
        
def Append(L,x): 
    # Inserts x at end of list L
    if IsEmpty(L):
        L.head = Node(x)
        L.tail = L.head
    else:
        L.tail.next = Node(x)
        L.tail = L.tail.next
        
def Print(L):
    # Prints list L's items in order using a loop
    temp = L.head
    while temp is not None:
        print(temp.item, end=' ')
        temp = temp.next
    print()  # New line 

def PrintRec(L):
    # Prints list L's items in order using recursion
    PrintNodes(L.head)
    print() 
    
def Remove(L,x):
    # Removes x from list L
    # It does nothing if x is not in L
    if L.head==None:
        return
    if L.head.item == x:
        if L.head == L.tail: # x is the only element in list
            L.head = None
            L.tail = None
        else:
            L.head = L.head.next
    else:
         # Find x
         temp = L.head
         while temp.next != None and temp.next.item !=x:
             temp = temp.next
         if temp.next != None: # x was found
             if temp.next == L.tail: # x is the last node
                 L.tail = temp
                 L.tail.next = None
             else:
                 temp.next = temp.next.next
         
def PrintReverse(L):
    # Prints list L's items in reverse order
    PrintNodesReverse(L.head)
    print()     
# Create a clone of the linked list 
def Copy(L):
    temp = L.head
    new_copy = List()
    while temp != None:
        Append(new_copy, temp.item)
        temp = temp.next

    return new_copy  
# Obtain item by traversing through the list
def ElementAt(L,x):
    temp = L.head

    for i in range(x):
        temp = temp.next

    return temp.item
# Get the size of the Linked list
def GetLength(L):
    temp = L.head
    i = 0
    while temp != None:
        i += 1
        temp = temp.next

    return i

def Median(L):
    C = Copy(L)
    return ElementAt(C,GetLength(C)//2)
# Create random list of integers
def random_list():
    L = List()
    for x in range(5):
        n = random.randint(0,46)
        Append(L, n)
    return L

# Bubble sort algorithm
def Bubble_sort(L):
    if IsEmpty(L):
        return

    if L.head != None and L.head.next == None :
        return L.head.item

    if L != None:
        temp = L.head
        is_sorting = True
        while is_sorting:
            temp = L.head
            is_sorting = False
            while temp.next != None:
                if temp.item > temp.next.item:
                    is_sorting = True
                    int_temp = temp.item
                    temp.item = temp.next.item
                    temp.next.item = int_temp
                temp = temp.next

    return Median(L)

def Split_list(L):
    if L == None:
        return L
    after = L.next
    before = L

    while after != None:
        after = after.next
        if after != None:
            before = before.next
            after=after.next
    return before

def Merge(L,K):
    combined = None
    # If a list is shorter than the other
    if L == None:
        return K
    if K == None:
        return L
    # L is less than, therefore L is inserted first
    if L.item <= K.item:
        combined = L
        combined.next = Merge(L.next, K) 
    #  K is less than, therefore K is inserted first
    else:
        combined = K
        combined.next = Merge(L, K.next) 

    return combined 

def Merge_sort(L):
    # If list is empty or only one element
    if L == None or L.next == None:
        return L

    if L != None:
        mid = Split_list(L)
        r = mid.next

        mid.next = None

        left = Merge_sort(L)
        right = Merge_sort(r)
        # j = Merge_sort(right)
        sorted_list = Merge(left,right)

        # final_list = List()
        # final_list.head = sorted_list
        return sorted_list
                
C = random_list()
# Print(C)

L = Copy(C)

# Print(L)
print(Bubble_sort(L))
# Print(L)

L = Copy(C)
# Print(L)
k = List()
k.head = Merge_sort(L.head)
print(Median(k))

