"""
Course: CS 2302
Author: Jacob Montenegro
Lab: 3
Instructor: Dr. Olac Fuentes
T.A.: Anindita Nath, Maliheh Zargaran
Date of Last Modification: 3/8/2019
Program's Purpose: Get aqcuainted with manipulating Binary Search Trees
"""
import matplotlib.pyplot as plt
import numpy as np
import math

class BST(object):
    #Constructor
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right
    
def Insert(T,newItem):
    if T == None:
        T = BST(newItem)
    elif T.item > newItem:
        T.left = Insert(T.left,newItem)
    else:
        T.right = Insert(T.right,newItem)
    return T

def InOrder(BST):
    if BST is not None:
        InOrder(BST.left)
        print(BST.item,end=' ')
        InOrder(BST.right)    

def PrintTree(BST,space):
    if BST is not None:
        PrintTree(BST.right,space+'   ')
        print(space,BST.item)
        PrintTree(BST.left,space+'   ')

def Height(BST):
    if BST is None:
        return -1
    LHeight = Height(BST.left) 
    RHeight = Height(BST.right)
    
    if LHeight > RHeight:
        return LHeight + 1
    else:
        return RHeight + 1

def NumOfNodes(BST):
    if BST is None:
        return 0
    return 1 + NumOfNodes(BST.left) + NumOfNodes(BST.right)

#Creates a balanced tree from a sorted list.
def BalTree(L):
    
    #Base-Case: checks if there are any elements in L, returns if empty
    if len(L)<=0:
        return
    #Finds the middle element
    root = (len(L))//2
    #makes middle element the head of the tree
    B = BST(L[root])
    #The left sub-tree is then created with each element before the middle element
    B.left = BalTree(L[:root])
    #The right sub-tree is then created with each element after the middle element
    B.right = BalTree(L[root+1:])
        
    #returns the completed balanced-tree
    return B

#Iterative version of Search function
def Search(T,c):

    while T is not None:
        #If T is None, the loop will break and return None, thus, c is not found.
        if T is None:
            break
        #Returns item if it's in T
        if c == T.item:
            return T.item
        if T is not None:
            #Searches right sub-tree if c is greater
            if c > T.item:
                T=T.right
        if T is not None:
            #Searches left sub-tree if c is lesser
            if c < T.item:
                    T=T.left
    return None

#This functon prints each element at each depth
def atDepth(T,d):
    #Checks if a tree exists
    if T is None:
        return -1
    print('Keys at depth',d,':',T.item,end=' ')
    print()
    d+=1
    atDepth(T.left,d)
    atDepth(T.right,d)
    
#This method draws a binary tree, it has an x,y, change in x (dx) and cahnge in y (dy), as well as a k.
#In this function, cx and cy are present, they serve the purpose of shifting each of the circles created,
#As well as shifting each element of the tree to their respective circles.
def draw_trees(ax,x,y,dx,dy,k,T,center,r,cx,cy):
    #This checks to see if a given tree has an element
    if T is not None:
        #This part focuses on producing the circles as well as the items
        q,t = circle(center,r)
        ax.plot(q+cx,t+dy-4-cy,linewidth=1,color='k')
        we = T.item
        font = {'family':'Times New Roman','color':'black','size':10}
        ax.text(center[0]-2.5+cx, center[1]+dy-cy-6,we, fontdict=font)
        
        if T.right is not None:
            #The ax.plot line prints a branch, the second ax.plot line prints a reflection of this ax.plot line.
            ax.plot(x*dx+2,y,linewidth=1,color='k')
            draw_trees(ax,x+k*dx,y-dy,dx/2,dy,k*4,T.right,center,r,cx+25*dx,cy+28)
            
        if T.left is not None:
            ax.plot(-x*dx-2,y,linewidth=1,color='k')
            #k is added since I noticed that the drawing kept shifting inward by multiples of 2, 4, 16, etc.
            #I realized that in order to shift left and right, I would need to continuously add and subtract dx by multiples of 4, which is why I am using k.
            draw_trees(ax,x-k*dx,y-dy,dx/2,dy,k*4,T.left,center,r,cx-25*dx,cy+28)

#This function was a given by Dr. Fuentes for the first lab.
def circle(center,rad):
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    return x,y

#This is an attempt to create a sorted list from a BST, this function should return a sorted list, instead it returns the left, right, then middle element of a subtree
def SortedList(T,L):
    #Base-Case, returns the list
    if T is None:
        return L
    #Iterates through left subtree(s)
    if T.left is not None:
        L[:-1] = SortedList(T.left,L[1:])
    #adds current node to end of list (This is because the last nodes to be added would be the root/right nodes)
    L[-1] = T.item
    #Iterates through the right subtree(s)
    if T.right is not None:
        L[:-1] = SortedList(T.right,L[1:])
    #returns list
    return L
  

T = None
A = [10,4,15,2,8,1,3,5,7,9,12,18]
for a in A:
    T = Insert(T,a)

plt.close("all") 
p = np.array([[0,20],[20,0]])
fig, ax = plt.subplots()
draw_trees(ax,p[0],p[1],1,28,52,T,[0,0],4,0,0)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
#fig.savefig('tree.png')

W = None
L = [1,2,3,4,5,6,7,8,9,10]
print('A sorted list:',L)
print('Into a balanced tree:')
W = BalTree(L)
PrintTree(W,'')

print()
d = 20
w = Search(T,d)
if w is None:
    print(d,': Not found')
else:
    print(d,': found')
print()

atDepth(T,0)
print()

Q = [None] * NumOfNodes(T)
B = SortedList(T,Q)
print('Sorted List:',B)