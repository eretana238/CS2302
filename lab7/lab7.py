# Course: 2302-001
# Author: Esteban Retana
# Assignment: 
# Instructor: Olac Fuentes
# TA: Eduardo Lara
# Date of last modification:4/16/19
# Purpose: 
import matplotlib.pyplot as plt
import numpy as np
import random
import time

def draw_maze(walls,maze_rows,maze_cols,cell_nums=False):
    fig, ax = plt.subplots()
    for w in walls:
        if w[1]-w[0] ==1: #vertical wall
            x0 = (w[1]%maze_cols)
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

def DisjointSetForest(size):
    return np.zeros(size,dtype=np.int)-1

def dsfToSetList(S):
    #Returns aa list containing the sets encoded in S
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

def NumSets(S):
    count =0
    for i in range(len(S)):
        if S[i]<0:
            count += 1
    return count

# Builds maze by removing walls without compression
def RemoveWalls(S,walls):
    # Gets total number of sets in forest
    sets = NumSets(S)
    r = []
    for i in range(sets):
        r = random.choice(walls)
        i = walls.index(r)
        # Checks if there is a pathalready
        if find(S,r[0]) != find(S,r[1]):
            # Eliminated random walls
            walls.pop(i)
            union(S,r[0],r[1])

# Builds maze by removing walls with compression
def RemoveWalls_c(S,maze_walls):
    # Gest total number of sets in forest
    sets = NumSets(S)
    r = []
    for i in range(sets):
        r = random.choice(walls)
        i = walls.index(r)
        # Checks if there is a path already
        if find(S,r[0]) != find(S,r[1]):
            # Eliminated random walls
            walls.pop(i)
            union_by_size(S,r[0],r[1])


plt.close("all") 
maze_rows = 10
maze_cols = 15

walls = wall_list(maze_rows,maze_cols)

# Displays original maze with cell numbers
draw_maze(walls,maze_rows,maze_cols,cell_nums=True) 

# Creates dfs with dimensions
fullSize = maze_rows * maze_cols
S = DisjointSetForest(fullSize)
# =============================================================================
# Maze generation without compression
# =============================================================================
start = time.time()

RemoveWalls(S,walls)

end = time.time()

removeWallTime = end - start

draw_maze(walls,maze_rows,maze_cols) 
print('Maze generation WITHOUT compression time:', removeWallTime)

# =============================================================================
# Maze generation with compression
# Uncomment this section and comment out the maze generation without compression to find running times 
# =============================================================================
#start2 = time.time()
#
#RemoveWalls_c(S,walls)
#
#end2 = time.time()
#
#removeWallTime2 = end2 - start2
#
#draw_maze(walls,maze_rows,maze_cols) 
#print('Maze generation WITH compression time:', removeWallTime2)
