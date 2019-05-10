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

def random_trig_func():
    x = random.choice(trig)
    return x

def trig_equality(tries=1000,tolerance=0.001):
    count = 0
    t = random.uniform(-math.pi,math.pi)
    for i in range(tries):
        s1 = random_trig_func()
        s2 = random_trig_func()
        x = eval(s1)
        y = eval(s2)
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

def partition(n):
    s = 0
    for i in n:
        s += i
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
    print('')