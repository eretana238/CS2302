# Course: 2302-001
# Author: Esteban Retana
# Assignment: Solve the maze from lab 6 (building maze with disjoint set forest)
# Instructor: Olac Fuentes
# TA: Mali and Dita
# Date of last modification:4/28/19
# Purpose: To be able to implement a maze solving algorithm such as Breadth First Search or Depth First Search and display its path

import matplotlib.pyplot as plt
import numpy as np
import random
import time

def DisjointSetForest(size):
    return np.zeros(size,dtype=np.int)-1

def dsfToSetList(S):
    #Returns a list containing the sets encoded in S
    sets = [ [] for i in range(len(S)) ]
    for i in range(len(S)):
        sets[find(S,i)].append(i)
    sets = [x for x in sets if x != []]
    return sets

def find(S,i):
    # Returns root of tree that i belongs to
    if S[i]<0:
        return i
    return find(S,S[i])

def find_c(S,i): #Find with path compression 
    if S[i]<0: 
        return i
    r = find_c(S,S[i]) 
    S[i] = r 
    return r
    
def union(S,i,j):
    # Joins i's tree and j's tree, if they are different
    ri = find(S,i) 
    rj = find(S,j)
    if ri!=rj:
        S[rj] = ri

def union_c(S,i,j):
    # Joins i's tree and j's tree, if they are different
    # Uses path compression
    ri = find_c(S,i) 
    rj = find_c(S,j)
    if ri!=rj:
        S[rj] = ri

def union_by_size(S,i,j):
    # if i is a root, S[i] = -number of elements in tree (set)
    # Makes root of smaller tree point to root of larger tree 
    # Uses path compression
    ri = find_c(S,i) 
    rj = find_c(S,j)
    if ri!=rj:
        if S[ri]>S[rj]: # j's tree is larger
            S[rj] += S[ri]
            S[ri] = rj
        else:
            S[ri] += S[rj]
            S[rj] = ri

def draw_maze(walls,maze_rows,maze_cols,maze_path,cell_nums=False):
    fig, ax = plt.subplots()
    for w in walls:
        if w[1]-w[0] == 1: #vertical wall
            x0 = (w[1] % maze_cols)
            x1 = x0
            y0 = (w[1]//maze_cols)
            y1 = y0+1
        else:#horizontal wall
            x0 = (w[0]%maze_cols)
            x1 = x0+1
            y0 = (w[1]//maze_cols)
            y1 = y0  
        ax.plot([x0,x1],[y0,y1],linewidth=1,color='k')
    sx = maze_cols
    sy = maze_rows
    ax.plot([0,0,sx,sx,0],[0,sy,sy,0,0],linewidth=2,color='k')
    if cell_nums:
        for r in range(maze_rows):
            for c in range(maze_cols):
                cell = c + r*maze_cols   
                ax.text((c+.5),(r+.5), str(cell), size=10,
                        ha="center", va="center")
    # Added maze path, displays line when its not empty
    if len(maze_path) != 0:
        # Check each connection and draw path
        for i in range(len(maze_path)-1):
            if maze_path[i+1]-maze_path[i]== maze_cols:
                x0 = (maze_path[i]%maze_cols)+.5
                x1 = x0
                y0 = (maze_path[i+1]//maze_cols)-.5
                y1 = y0+1

            elif maze_path[i+1]-maze_path[i]== -maze_cols: 
                x0 = (maze_path[i+1]%maze_cols)+.5
                x1 = x0
                y0 = (maze_path[i]//maze_cols)-.5
                y1 = y0+1
                
            elif maze_path[i+1]-maze_path[i] == -1:
                x0 = (maze_path[i+1]%maze_cols)+.5
                x1 = x0+1
                y0 = (maze_path[i]//maze_cols)+.5
                y1 = y0

            else:
                x0 = (maze_path[i]%maze_cols)+.5
                x1 = x0+1
                y0 = (maze_path[i+1]//maze_cols)+.5
                y1 = y0
            ax.plot([x0,x1],[y0,y1],linewidth=2,color='blue')
    ax.axis('off') 
    ax.set_aspect(1.0)


def wall_list(maze_rows, maze_cols):
    # Creates a list with all the walls in the maze
    w =[]
    for r in range(maze_rows):
        for c in range(maze_cols):
            cell = c + r*maze_cols
            if c!=maze_cols-1:
                w.append([cell,cell+1])
            if r!=maze_rows-1:
                w.append([cell,cell+maze_cols])
    return w

def NumSets(S):
    count =0
    for i in range(len(S)):
        if S[i]<0:
            count += 1
    return count

#finds the path to a vertex v and appends it to a list
def find_path(prev,v,a):
    if prev[v] != -1:
        find_path(prev,prev[v],a)
    a.append(v)
    return a   

# Builds maze by removing walls with compression
def RemoveWalls_c(S,Adj_list,m,walls):
    r = []
    w = len(walls)
    
    numCells = NumSets(S)
    Message(m,numCells) 
    for i in range(m):
        # Chooses random wall to remove
        r = random.choice(walls)
        f = walls.index(r)
        # Starts to remove random walls
        if i < numCells-1:   
            while True:
                if find(S,r[0]) != find(S,r[1]):
                    # Adjencency list build
                    build_adj_list(Adj_list,r[0],r[1])
                    # Eliminates random walls
                    walls.pop(f)
                    union_by_size(S,r[0],r[1])
                    break
                else:
                    r = random.choice(walls)
                    f = walls.index(r)
        else:   
            # Adjencency list build
            build_adj_list(Adj_list,r[0],r[1])
            # Eliminates random walls
            walls.pop(f)
            union_by_size(S,r[0],r[1])
            if i == w-1:
                print("Reached maximum number of walls to remove.")
                return

#Function to display messages based on m
def Message(m,walls):
    if m < walls-1:
        print("A path from source to destination is not guaranteed to exist.")
    elif m == walls-1:
        print("There is a unique path from source to destination.")
    else:
        print("There is at least one path from source to destination.")

# Creates adjencency list
def build_adj_list(Adj_list,s1,s2):
    Adj_list[s1].append(s2)
    Adj_list[s2].append(s1)

# Searches for solution using Breadth First Search
def BFS(G,v):
    visited = [False] * len(G)
    prev = [-1] * len(G)
    Q = []
    Q.append(v)
    visited[v] = True
    # Does loop while the Q is not empty
    while len(Q) != 0:
        # Obtains first value
        u = Q.pop(0)
        # Visits every vertex from index obtained
        for t in G[u]:
            if visited[t] == False:
                visited[t] = True
                prev[t] = u
                Q.append(t)
    return prev

# Searches for solution using Depth First Search
def DFS(G,source):
    visited[source] = True
    # Visits every vertex from source
    for t in G[source]:
        if not visited[t]:
            prev[t] = source
            DFS(G,t)

# Searches for solution using Depth First Search
def DFS_iter(G,source):
    visited = [False] * len(G)
    prev = [-1] * len(G)
    stack = []
    stack.append(source)
    visited[source] = True
    # Does loop while the stack is not empty
    while len(stack) != 0:
        # Obtains first value
        u = stack.pop(-1)
        # Visits every vertex from index obtained
        for t in G[u]:
            if visited[t] == False:
                visited[t] = True
                prev[t] = u
                stack.append(t)
    return prev

plt.close("all")
maze_rows = 15
maze_cols = 15

walls = wall_list(maze_rows,maze_cols)

# Displays original maze with cell numbers
draw_maze(walls,maze_rows,maze_cols,[],cell_nums=True)

# Creates dfs with dimensions
n = maze_rows * maze_cols
S = DisjointSetForest(n)

print("Amount of cells (n):",n)
m = int(input("Enter the number of walls to be removed: "))

# Adjancency list build
Adj_list = [[] for i in range(n)]

RemoveWalls_c(S,Adj_list,m,walls)

#Breadth first search
print("Building Breadth First Search path....")
start = time.perf_counter_ns()
path = BFS(Adj_list,0)
end = time.perf_counter_ns()
print("Breadth First Search time:",end-start,end="ns\n")

maze_path = find_path(path,len(Adj_list)-1,[])

draw_maze(walls, maze_rows, maze_cols,maze_path,cell_nums=False)

#Depth First Search
visited = [False] * len(Adj_list)
prev = [-1] * len(Adj_list)

print("Building Depth First Search WITH recursion path....")
start = time.perf_counter_ns()
DFS(Adj_list,0)
end = time.perf_counter_ns()
print("Depth First Search time:",end-start,end="ns\n")

maze_path = find_path(prev,len(Adj_list)-1,[])

draw_maze(walls, maze_rows, maze_cols,maze_path,cell_nums=False)

#Depth First Search iterably
print("Building Depth First Search WITHOUT recursion path....")
start = time.perf_counter_ns()
path = BFS(Adj_list,0)
end = time.perf_counter_ns()
print("Time for Depth First Search:",end-start,end="ns\n")

maze_path = find_path(path,len(Adj_list)-1,[])

draw_maze(walls, maze_rows, maze_cols,maze_path,cell_nums=False)