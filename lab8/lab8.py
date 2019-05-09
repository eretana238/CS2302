# Course: 2302-001
# Author: Esteban Retana
# Assignment: Write a program to discover trigonometric identities, and find if there is a valid partition on a given set
# Instructor: Olac Fuentes
# TA: Mali and Dita
# Date of last modification:4/28/19
# Purpose: Use randomized algorithms to check equality between two trig identities and use backtracking to find a valid partition

import random
import numpy as np
from math import *
from mpmath import sec
import math

trig = [
    'sin(t)',
    'cos(t)',
    'tan(t)',
    'sec(t)',
    '-sin(t)',
    '-cos(t)',
    '-tan(t)',
    'sin(-t)',
    'cos(-t)',
    'tan(-t)',
    'sin(t)/cos(t)',
    '2*sin(t/2)*cos(t/2)',
    'sin(t)**2',
    '1-cos(t)**2',
    '(1-cos(t)**2)/2',
    '1/cos(t)'
]

# Creates random choice of trig function
def random_trig_func():
    x = random.choice(trig)
    return x

# Chooses two trig functions and compares them to determine if they're similar
def trig_equality(tries=1000,tolerance=0.001):
    count = 0
    t = random.uniform(-math.pi,math.pi)
    for i in range(tries):
        # Assigns random trig function to s1 and s2
        s1 = random_trig_func()
        s2 = random_trig_func()
        # Obtain answer from trig function
        x = eval(s1)
        y = eval(s2)
        # figures out if both trig identities are similar
        if np.abs(x-y) < tolerance:
            count += 1
            print(s1,"|",s2,"| Count:",count)
    print()
    return count

def subsetsum(S,last,goal):
    if goal ==0:
        return True, []
    if goal<0 or last<0:
        return False, []
    res, subset = subsetsum(S,last-1,goal-S[last]) # Take S[last]
    if res:
        subset.append(S[last])
        return True, subset
    else:
        return subsetsum(S,last-1,goal) # Don't take S[last]

# Finds out if there's partition in set
def partition(n):
    s = 0
    # Finds sum of n
    for i in n:
        s += i
    # Determines if sum is odd, then its false
    if s % 2 != 0:
        return False

    goal = s // 2
    return goal

print("Number of similar trig functions:",trig_equality())

S = [2,4,5,9,12]
p = partition(S)
a,s2 = subsetsum(S,len(S)-1,p)
s1 = []
if p:
    for i in S:
        if i not in s2:
            s1.append(i)
    print('s1:',s1)
    print('s2:',s2)
else:
    print('Set does not contain partition')
