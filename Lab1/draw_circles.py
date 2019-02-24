# Course: 2302-001
# Author: Esteban Retana
# Assignment: Create figures or fractals based on the knowledge of recursion
# Instructor: Olac Fuentes
# TA: Eduardo Lara
# Date of last modification:2/8/19
# Purpose: Practice creating fractals with recursion

import matplotlib.pyplot as plt
import numpy as np
import math 
import time

def circle(center,rad):
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)+rad
    y = center[1]+rad*np.cos(t)
    return x,y

def circle2(center,rad):
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    return x,y

def looping_circles(ax,n,center,radius,w):
    if n>0:
        x,y = circle(center,radius)
        ax.plot(x,y,color='k')
        looping_circles(ax,n-1,center,radius*w,w)
      
def quad_inner_circles(ax,n,middle_x,middle_y,r):
    if n>0:
        middle = [middle_x,middle_y]
        x,y = circle2(middle,r)
        ax.plot(x,y,color='k')
        shift = r * (2/3)
        left = middle_x + shift
        right = middle_x - shift
        up = middle_y + shift
        down = middle_y - shift
        r /= 3
        quad_inner_circles(ax,n-1,left,middle_y,r)
        quad_inner_circles(ax,n-1,right,middle_y,r)
        quad_inner_circles(ax,n-1,middle_x,up,r)
        quad_inner_circles(ax,n-1,middle_x,down,r)
        quad_inner_circles(ax,n-1,middle_x,middle_y,r)
        
# Comment the other figures except the one you want to view
start_time = time.time()
plt.close("all") 
fig, ax = plt.subplots() 
#looping_circles(ax, 100, [100,0], 100,.9)
#ax.set_aspect(1.0)
#ax.axis('off')
#plt.show()
#fig.savefig('circlesa.png')


#looping_circles(ax, 30, [100,0], 100,.8)
#ax.set_aspect(1.0)
#ax.axis('off')
#plt.show()
#fig.savefig('circlesb.png')


#looping_circles(ax, 30, [100,0], 100,.9)
#ax.set_aspect(1.0)
#ax.axis('off')
#plt.show()
#fig.savefig('circlesc.png')

quad_inner_circles(ax,5,0,0,200)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('quad-inner-circlesa.png')

#quad_inner_circles(ax,4,0,0,200)
#ax.set_aspect(1.0)
#ax.axis('off')
#plt.show()
#fig.savefig('quad-inner-circlesb.png')

#quad_inner_circles(ax,5,0,0,200)
#ax.set_aspect(1.0)
#ax.axis('off')
#plt.show()
#fig.savefig('quad-inner-circlesc.png')
end_time = time.time() - start_time
print(end_time)