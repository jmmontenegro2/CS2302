"""
Course: CS 2302
Author: Jacob Montenegro
Lab: 8
Instructor: Dr. Olac Fuentes
T.A.: Anindita Nath, Maliheh Zargaran
Date of Last Modification: 5/8/2019
Program's Purpose: Certain algorithms attribute to feasible solutions through
                    Randomization and Backtracking, this assignemnt ensures that
                    different algorithms are understood. Produce a list of 
                    trigonometric equalities to practice with 
                    Randomizatiion. Find a partition (if possible) using 
                    Backtracking and show whether a partition exists or not.
"""

import random
from math import *
import numpy as np
from mpmath import *

#This function is used to append equal identities to a list
def DiscoverIdentities(TrigID):
    equal = []
    tries = 100
    while tries > 0:
        F1 = random.randint(0,len(TrigID)-1)
        F2 = random.randint(0,len(TrigID)-1)
        if TrigID[F1] != TrigID[F2] and Equal(TrigID[F1],TrigID[F2]):
            equal.append([TrigID[F1],TrigID[F2]])
            
        tries -= 1
    return equal

#This function is used to determine if two functions are equal
def Equal(f1,f2,tries=1000,tolerance=0.0001):
    for i in range(tries):
        #selects a random number from the pi to -pi range
        t = random.uniform(-pi, pi)
        y1 = eval(f1)
        y2 = eval(f2)
        #This function is boolean function that returns True if the functions are equal, False otherwise.
        if np.abs(y1-y2)>tolerance:
            return False
    return True

#This list contains all the trigonometric identities
trigID = ['sin(t)','cos(t)','tan(t)','sec(t)','-sin(t)','-cos(t)','-tan(t)',
          'sin(-t)','cos(-t)','tan(-t)','sin(t)/cos(t)','2*sin(t/2)*cos(t/2)',
          'sin(t)*sin(t)','1-(cos(t)*cos(t))','(1-cos(2*t))/2','1/cos(t)']

#Returns the list of equal identities
e = DiscoverIdentities(trigID)

#prints the list of equal identities
print('\n\nEqualities:\n')
for i in range(len(e)):
    for j in range(len(e[i])):
        print(e[i][j],end='  ')
    print()
    
#returns True if the sums of the two lists are equal, False otherwise
def Partition(S1,S2):
    return sum(S1) == sum(S2)

#This function traverses across the Set S (its numbers) and returns True and saves 2 sets that add up to goal
#or returns False if goal or last are negative 
#All insert functions are set to 0 (First item in list) to ensure the lists are sorted
def SubsetSum(S,last,goal):
    #These global variables store the values of the set S, they are the partition
    global s1
    global s2
    
    #Here, we are adding the first element of the list if we've found that last is equal to 0
    if last == 0:
        s1.insert(0,S[last])
    #We return true if we've met our goal
    if goal == 0:
        return True
    #We return False if both goal and last are negative numbers
    if last < 0 or goal < 0:
        return False
    #Checks if the current element in the list is of use to the partition and saves it to the second list
    #Not appending the integer otherwise
    if SubsetSum(S,last-1,goal-S[last]):
        s2.append(S[last])
        return True
    #inserts the current item into the first list
    s1.insert(0,S[last])
    #returns the function and moves to next element in list
    return SubsetSum(S,last-1,goal)

print('----------------------------------------------')
#initializes the global lists
global s1
global s2
s1 = []
s2 = []

#Initializes the Set
S = [2,4,5,9,12]

#Checks if a partition exists: checks that 2 sets of numbers from the list
#add up to the length of the set divided by 2, then checks that all elements are used 
#(ensuring that this is a true partition)
if SubsetSum(S,len(S)-1,sum(S)/2) and (len(s1) + len(s2)) == len(S):
    #prints the 2 subsets if a partition exists
    print('Partition:\n')
    print(s1)
    print(s2)
else:
    #prints that no partition exists
    print('No partition exists')