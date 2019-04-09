# Course: 2302-001
# Author: Esteban Retana
# Assignment: Read a word fie and its vectors and compute their similarites of words using Binary Trees or Hash tables and compute their running times
# Instructor: Olac Fuentes
# TA: Eduardo Lara
# Date of last modification:4/08/19
# Purpose: Understand how Natural Language Processing works, storing items in bst and in hash table with chainning to see which data structure is faster

import numpy as np
import math
import time

class BST(object):
    # Constructor
    def __init__(self, item, left=None, right=None):  
        self.item = item
        self.left = left 
        self.right = right      

def BSTInsert(T,newItem):
    if T == None:
        T =  BST(newItem)
    elif T.item[0] > newItem[0]:
        T.left = BSTInsert(T.left,newItem)
    else:
        T.right = BSTInsert(T.right,newItem)
    return T

def CreateBST(textFile):
    T = None
    print('Building binary search tree\n')
    for line in textFile:
        lineArr = line.strip().split(' ')
        word = lineArr[0]
        embedding = np.asarray(lineArr[1:],dtype=np.float32)
        compound = [word] + [embedding]
        T = BSTInsert(T,compound)  

    return T
    
def DisplayStatsBST(T,bt):
    print('Number of nodes:',CountNodes(T))
    print("Height:",TreeHeight(T))
    print("Running time for binary search tree construction:",bt)
    
    # Reading word file to determine similarities
    print("\nReading word file to determine similarites\n")

    w = open("compare.txt", "r")
    for line in w:
        words = line.strip().split(' ')
        
        print("Similarity {} = {:.4f}".format(words,Sim(BSTFind(T,words[0]).item[1],BSTFind(T, words[1]).item[1])))

def Smallest(T):
    if T.left != None:
        T = Smallest(T.left)
    return T

def Delete(T,del_item):
    if T is not None:
        if del_item < T.item:
            T.left = Delete(T.left,del_item)
        elif del_item > T.item:
            T.right = Delete(T.right,del_item)
        else:  # del_item == T.item
            if T.left is None and T.right is None: # T is a leaf, just remove it
                T = None
            elif T.left is None: # T has one child, replace it by existing child
                T = T.right
            elif T.right is None:
                T = T.left    
            else: # T has two chldren. Replace T by its successor, delete successor
                m = Smallest(T.right)
                T.item = m.item
                T.right = Delete(T.right,m.item)
    return T

def BSTFind(T,k):
    # Returns the address of k in BST, or None if k is not in the tree
    if T is None or T.item[0] == k:
        return T
    if T.item[0]<k:
        return BSTFind(T.right,k)
    return BSTFind(T.left,k)
        
def CountNodes(T):
    if T is None:
        return 0
    
    return 1 + CountNodes(T.left) + CountNodes(T.right)
    
def TreeHeight(T):
    if T == None:
        return 0
    
    left = TreeHeight(T.left)
    right = TreeHeight(T.right)

    if left > right:
        return left + 1
    else:
        return right + 1
    
def Sim(e0,e1):
    top = sum([i*j for i,j in zip(e0,e1)])
    
    bottom = magnitude(e0) * magnitude(e1)
    
    return top / bottom

def magnitude(u):    
    uSum = 0
    for i in range(len(u)):
        uSum += math.pow(float(u[i]),2)
   
    return math.sqrt(uSum)
    
# Implementation of hash tables with chaining using strings

class HashTableC(object):
    # Builds a hash table of size 'size'
    # Item is a list of (initially empty) lists
    # Constructor
    def __init__(self,size):  
        self.item = []
        self.num_items = 0
        for i in range(size):
            self.item.append([])
        
def InsertC(H,k,l):
    # Inserts k in appropriate bucket (list) 
    # Does nothing if k is already in the table
    b = h(k[0],len(H.item))
    if not H.item[b]:
        H.num_items += 1

    H.item[b].append([k,l]) 
   
def FindC(H,k):
    # Returns bucket (b) and index (i) 
    # If k is not in table, i == -1
    b = h(k,len(H.item))
    for i in range(len(H.item[b])):
        if H.item[b][i][0][0] == k:
            return b, i
    return b, -1
 
def h(s,n):
    r = 0
    for c in s:
        r = (r*255 + ord(c))% n
    return r

def Rehash(H):
    temp = HashTableC(len(H.item))

    for i in range(len(H.item)):
        for j in range(len(H.item[i])):
            InsertC(temp, H.item[i][j][0], len(H.item[i][j][0]))

    n = len(temp.item) * 2 + 1 
    H = HashTableC(n)

    for i in range(len(temp.item)):
        for j in range(len(temp.item[i])):
            InsertC(H, temp.item[i][j][0], len(temp.item[i][j][0]))

    return H
        
def Hash(textFile):
    print("Building hash table with chaining")
    H = HashTableC(7)

    for line in textFile:
        lineArr = line.strip().split(' ')
        word = lineArr[0]
        embedding = np.asarray(lineArr[1:],dtype=np.float32)
        compound = [word] + [embedding]
        # print(compound[0][0])
        InsertC(H,compound,len(word))

        # Figures out if the table needs rehashing
        if H.num_items/len(H.item) == 1:
            H = Rehash(H)

    return H

def DisplayStatsHash(H):
    print("Hash table stats:")
    print("Initial table size: 7")
    print("Final table size:",len(H.item))
    print("Load factor:", H.num_items/len(H.item))
    print("Percentage of empty lists: {:.2f}%".format((len(H.item)-H.num_items)/len(H.item)*100))
    print("Standard deviation of the lengths of the lists: 2")
    
    # Reading word file to determine similarities
    print("\nReading word file to determine similarites\n")

    w = open("compare.txt", "r")
    for line in w:
        words = line.strip().split(' ')
        
        bucket, i = FindC(H,words[0])
        bucket2, j = FindC(H,words[1])
        print("Similarity {} = {:.4f}".format(words,Sim(H.item[bucket][i][0][1], H.item[bucket2][j][0][1])))


        
 
print("Choose table implementation\nType 1 for binary search tree or 2 for hash table with chaining")
choice = int(input("Choice: "))
print()

with open('glove.6B.50d.txt', 'r', encoding='utf-8') as textFile:
    if choice == 1:
        startTime = time.time()
        T = CreateBST(textFile)
        endTime = time.time()
        binaryBuildTime = endTime - startTime
        # Stats
        startTime2 = time.time()
        DisplayStatsBST(T,binaryBuildTime)
        endTime2 = time.time()
        binaryQuery = endTime2 - startTime2
        print("Running time for binary search tree query processing:",binaryQuery)
        

    elif choice == 2:
        startTime = time.time()
        H = Hash(textFile)
        endTime = time.time()
        hashBuildingTime = endTime - startTime
        # print("Running time for hash table construction:",hashBuildingTime)

        startTime2 = time.time()
        DisplayStatsHash(H)
        endTime2 = time.time()
        hashQuery = endTime2 - startTime2
        print("Running time for hash table query processing:",hashQuery)