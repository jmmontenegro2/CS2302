"""
Course: CS 2302
Author: Jacob Montenegro
Lab: 1
Instructor: Dr. Olac Fuentes
T.A.: Anindita Nath, Maliheh Zargaran 
Date of Last Modification: 2/8/2019
Program's Purpose: Practice using recursion to produce figures.
"""
import numpy as np
import matplotlib.pyplot as plt
import math

#draw_squares recursively draws squares on every corner of a given square, the depth being n, the number of times to recursively call the method
def draw_squares(ax,n,p,w,z):
    if n>0:
        #These two lines of code give the Original Square four corners.
        ax.plot(p[:,0]/2-z,p[:,1]/2-z,linewidth=1,color='k')
        ax.plot(-p[:,0]/2+z,p[:,1]/2-z,linewidth=1,color='k')
    #The if statement ensures that the recursive call doesn't produce more squares than necessary.
    if n>1:
        #The next four lines of code produce miniture squares for the previously produces squares at each corner.
        #They are dividing by 4 since that is half the size of the previously created squares. 
        ax.plot(-p[:,0]/4,-p[:,1]/4+z,linewidth=1,color='k') 
        ax.plot(p[:,0]/4,-p[:,1]/4+z,linewidth=1,color='k') 
        ax.plot(-p[:,0]/4+z,-p[:,1]/4,linewidth=1,color='k') 
        ax.plot(p[:,0]/4-z,-p[:,1]/4,linewidth=1,color='k')
        #These recursive calls ensure that z alternates between negative ten and positive ten, z (10) is used to shift the squares left, right, up, and down.
        draw_squares(ax,n-1,p*w,w,z)
        draw_squares(ax,n-1,-p*w,w,-z)
        draw_squares(ax,n-1,-p*w,w,z-z)
        
#The circle method/function was given by Dr. Fuentes, it creates the circle.
def circle(center,rad):
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    return x,y

#This method produces circles shifting to the left along the perimeter of every previous circle.
def draw_Spiralcircles(ax,n,center,radius,w):
    if n>0:
        x,y = circle(center,radius)
        #I used x+radius here to shift every circle left, adding to x within a function shifts a given graph left.  
        ax.plot(x+radius,y,linewidth=1,color='k')
        draw_Spiralcircles(ax,n-1,center,radius*w,w)

#This method draws a binary tree, it has an x,y, change in x (dx) and cahnge in y (dy), as well as a k.
def draw_trees(ax,n,x,y,dx,dy,k):
    if n>0:
        #The first line prints a branch, the second line prints a reflection of the first line.
        ax.plot(x*dx,y,linewidth=1,color='k')
        ax.plot(-x*dx,y,linewidth=1,color='k')
        #k is added since I noticed that the drawing kept shifting inward by multiples of 2, 4, 16, etc.
        #I realized that in order to shift left and right, I would need to continuously add and subtract dx by multiples of 4, which is why I am using k.
        draw_trees(ax,n-1,x+k*dx,y-dy,dx/2,dy,k*4)
        draw_trees(ax,n-1,x-k*dx,y-dy,dx/2,dy,k*4)
        
#draw_circles produces a circle with 5 circles within it, recursively.
def draw_circles(ax,n,center,radius,w):
    if n>0:
        x,y = circle(center,radius)
        #x and why are multiplying by 3 to ensure the first circle engulfs the next five.
        ax.plot(x*3,y*3,linewidth=1,color='k')
        #This if statement prevents any extra circles from being drawn.
        if n>1:
            ax.plot(x+radius+100,y,linewidth=1,color='k')
            ax.plot(x-radius+300,y,linewidth=1,color='k')
            ax.plot(x+200,y-radius+100,linewidth=1,color='k')
            ax.plot(x+200,y+radius-100,linewidth=1,color='k')
            miniCircles(x,y,radius)
        #The circles fit along the diameter of the engulfing circle, thats why radius is divided by 3 at each recursive call.
        draw_circles(ax,n-1,center,radius/3,w)
      
def miniCircles(x,y,radius):
    #Produces right circle
    ax.plot(x+200,y,linewidth=1,color='k')
    
    #Produces left circle
    ax.plot(x-200,y,linewidth=1,color='k')
    ax.plot(x+radius-300,y,linewidth=1,color='k')
    ax.plot(x-radius-100,y,linewidth=1,color='k')
    ax.plot(x-200,y-radius+100,linewidth=1,color='k')
    ax.plot(x-200,y+radius-100,linewidth=1,color='k')
    
    #Produces center circle
    ax.plot(x+radius-100,y,linewidth=1,color='k')
    ax.plot(x-radius+100,y,linewidth=1,color='k')
    ax.plot(x,y-radius+100,linewidth=1,color='k')
    ax.plot(x,y+radius-100,linewidth=1,color='k')
    
    #Produces top circle
    ax.plot(x,y+200,linewidth=1,color='k')
    ax.plot(x+radius-100,y+200,linewidth=1,color='k')
    ax.plot(x-radius+100,y+200,linewidth=1,color='k')
    ax.plot(x,y-radius+300,linewidth=1,color='k')
    ax.plot(x,y+radius+100,linewidth=1,color='k')
    
    #Produces bottom circle
    ax.plot(x,y-200,linewidth=1,color='k')
    ax.plot(x+radius-100,y-200,linewidth=1,color='k')
    ax.plot(x-radius+100,y-200,linewidth=1,color='k')
    ax.plot(x,y-radius-100,linewidth=1,color='k')
    ax.plot(x,y+radius-300,linewidth=1,color='k')

"""Square Section""" 
#Square 1         
plt.close("all") 
orig_size = 10
p = np.array([[30,30],[orig_size,30],[orig_size,orig_size],[30,orig_size],[30,30]])
fig, ax = plt.subplots()
draw_squares(ax,2,p,.5,10)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('squares.png')

#Square 2
plt.close("all") 
orig_size = 10
p = np.array([[30,30],[orig_size,30],[orig_size,orig_size],[30,orig_size],[30,30]])
fig, ax = plt.subplots()
draw_squares(ax,3,p,.5,10)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('squares1.png')

#Square 3
plt.close("all") 
orig_size = 10
p = np.array([[30,30],[orig_size,30],[orig_size,orig_size],[30,orig_size],[30,30]])
fig, ax = plt.subplots()
draw_squares(ax,4,p,.5,10)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('squares2.png')
      
"""Spiral Circle Section"""
#Spiraling Circle 1
plt.close("all") 
fig, ax = plt.subplots() 
draw_Spiralcircles(ax, 9, [0,0], 100,.5)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('circles.png')

#Spiraling Circle 2
plt.close("all") 
fig, ax = plt.subplots() 
draw_Spiralcircles(ax, 50, [50,0], 100,.9)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('circles1.png')

#Spiraling Circle 3
plt.close("all") 
fig, ax = plt.subplots() 
draw_Spiralcircles(ax, 85, [50,0], 100,.95)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('circles2.png')

"""Tree Section"""
#Tree 1
plt.close("all") 
orig_size = 10
p = np.array([[0,1],[1,0]])
fig, ax = plt.subplots()
draw_trees(ax,3,p[0],p[1],1,1,2 )
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('tree.png')

#Tree 2
plt.close("all") 
orig_size = 10
p = np.array([[0,1],[1,0]])
fig, ax = plt.subplots()
draw_trees(ax,4,p[0],p[1],1,1,2)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('tree1.png')

#Tree 3
plt.close("all") 
orig_size = 10
p = np.array([[0,1],[1,0]])
fig, ax = plt.subplots()
draw_trees(ax,7,p[0],p[1],1.5,1,1.34)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('tree2.png')

"""Circle Section"""
#Circle 1
plt.close("all") 
fig, ax = plt.subplots() 
draw_circles(ax, 3, [0,0], 100,.5)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('circlesOfCircles.png')

#Circle 2
plt.close("all") 
fig, ax = plt.subplots() 
draw_circles(ax, 4, [0,0], 100,.5)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('circlesOfCircles1.png')

#Circle 3
plt.close("all") 
fig, ax = plt.subplots() 
draw_circles(ax, 5, [0,0], 100,.5)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('circlesOfCircles2.png')