"""
Course: CS 2302
Author: Jacob Montenegro
Lab: 6
Instructor: Dr. Olac Fuentes
T.A.: Anindita Nath, Maliheh Zargaran
Date of Last Modification: 4/12/2019
Program's Purpose: Use disjoint set forests to produce optimized maze of one set
"""

# Implementation of disjoint set forest 
# Programmed by Olac Fuentes
# Last modified March 28, 2019
import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate 
import random

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

def draw_dsf(S):
    scale = 30
    fig, ax = plt.subplots()
    for i in range(len(S)):
        if S[i]<0: # i is a root
            ax.plot([i*scale,i*scale],[0,scale],linewidth=1,color='k')
            ax.plot([i*scale-1,i*scale,i*scale+1],[scale-2,scale,scale-2],linewidth=1,color='k')
        else:
            x = np.linspace(i*scale,S[i]*scale)
            x0 = np.linspace(i*scale,S[i]*scale,num=5)
            diff = np.abs(S[i]-i)
            if diff == 1: #i and S[i] are neighbors; draw straight line
                y0 = [0,0,0,0,0]
            else:      #i and S[i] are not neighbors; draw arc
                y0 = [0,-6*diff,-8*diff,-6*diff,0]
            f = interpolate.interp1d(x0, y0, kind='cubic')
            y = f(x)
            ax.plot(x,y,linewidth=1,color='k')
            ax.plot([x0[2]+2*np.sign(i-S[i]),x0[2],x0[2]+2*np.sign(i-S[i])],[y0[2]-1,y0[2],y0[2]+1],linewidth=1,color='k')
        ax.text(i*scale,0, str(i), size=20,ha="center", va="center",
         bbox=dict(facecolor='w',boxstyle="circle"))
    ax.axis('off') 
    ax.set_aspect(1.0)

# Starting point for program to build and draw a maze
# Modify program using disjoint set forest to ensure there is exactly one
# simple path joiniung any two cells
# Programmed by Olac Fuentes
# Last modified March 28, 2019

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

#checks if items in same set
def SameSet(S,i,j):
    return find(S,i) == find(S,j)

#sameSet with path compression
def SameSet_c(S,i,j):
    return find_c(S,i) == find_c(S,j)

def numSets(S):
    c = 0
    for s in S:
        if s < 0:
            c += 1
    return c
#returns the indices of roots
def getIndex(S):
    index = 0
    L = []
    for s in S:
        index += 1
        if s < 0:
            L.append(index)
    return L
#Standard union and find
def Standard():
    
    plt.close("all") 
    maze_rows = 10
    maze_cols = 15
    
    walls = wall_list(maze_rows,maze_cols)
    S = DisjointSetForest(maze_rows*maze_cols)
    i = 0
    draw_maze(walls,maze_rows,maze_cols,cell_nums=True) 
    # this is set to 25 because the program never reaches just 1 set, it stops around 20 and 30 total sets
    # this ensures that the program does not enter an infinite loop
    while numSets(S) > 25:
        #random number chosen from the list
        d = random.randint(0,len(S)-1)
        
        #ensures that the index is within that of the walls list
        if d < len(walls):
            #checks that the numbers do not belong to the same set
            if SameSet(S,d,walls[d][0]) is False:
                #unites them if they're not in the same set
                union(S,d,walls[d][0])
                #removes the wall
                walls.pop(d)
    #returns the indices of all the negative numbers
    L = getIndex(S)
    
    i = 0
    while numSets(S) > 10 and len(L) > 15:
        #ensures that the loop never enters an infinite loop
        if i == 50000:
            break
        i += 1        
        #selects a random number
        d = random.randint(0,max(L))
        if d < len(walls):
            #loops through the indexes that have not been united yet
            for l in L:
                if l < len(walls) and SameSet(S,walls[l][0],walls[d][0]) is False:
                    union(S,walls[l][0],walls[d][0])
                    walls.pop(d)
                    L.remove(l)
        #shuffles the item
        random.shuffle(L)

    draw_maze(walls,maze_rows,maze_cols) 

#Method for union by size and compression
def BySizeComp():
    
    plt.close("all") 
    maze_rows = 10
    maze_cols = 15
    
    walls = wall_list(maze_rows,maze_cols)
    S = DisjointSetForest(maze_rows*maze_cols)
    i = 0
    draw_maze(walls,maze_rows,maze_cols,cell_nums=True) 
    #set to 30 to ensure that the loop doesn't enter an infinite loop
    while numSets(S) > 30:
        i += 1  
        #chooses random number
        d = random.randint(0,len(S)-1)
        
        if d < len(walls):
            if SameSet_c(S,d,walls[d][0]) is False:
                union_by_size(S,d,walls[d][0])
                walls.pop(d)
    #list of all the indices that may or may not have been combined in union with other sets 
    L = getIndex(S)
    
    i = 0
    while numSets(S) > 25 and len(L) > 10:
        #selects a random number
        d = random.randint(0,len(L)-1)
        if d < len(walls):
            #checks that the items are not in the same set 
            if L[0] < len(walls) and SameSet_c(S,L[0],walls[d][0]) is False:
                union_by_size(S,L[0],walls[d][0])
                walls.pop(d)
                #ensures that the removed item is not repeated
                L.remove(L[0])
        #randomizes the list to ensure that a new item is chosen each iteration
        random.shuffle(L)
    
    draw_maze(walls,maze_rows,maze_cols) 


Standard()

BySizeComp()
