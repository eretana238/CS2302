# Course: 2302-001
# Author: Esteban Retana
# Assignment: Create figures or fractals based on the knowledge of recursion
# Instructor: Olac Fuentes
# TA: Eduardo Lara
# Date of last modification:2/8/19
# Purpose: Practice creating fractals with recursion

import numpy as np
import matplotlib.pyplot as plt

def draw_squares(ax,n,p,w):
    if n>0:
        i1 = [1,2,3,0,1]
        q = p*w + p[i1]*(1-w)
        ax.plot(p[:,0],p[:,1],color='k')
        draw_squares(ax,n-1,q,w)
        
    # Creates square pattenr based on each vertex as a median point
def pattern(ax,n,x,y,size):
    if n>0:        
        right_x = x+size
        left_x = x-size
        lower_y = y-size
        upper_y = y+size
        # Creates new square
        q = np.array([[left_x,lower_y],[left_x,upper_y],[right_x,upper_y],[right_x,lower_y],[left_x,lower_y]])
        
        ax.plot(q[:,0],q[:,1],color='k')
        
        # bottom left
        pattern(ax,n-1,left_x,lower_y,size/2) 
        # upper left
        pattern(ax,n-1,left_x,upper_y,size/2) 
        # upper right
        pattern(ax,n-1,right_x,upper_y,size/2) 
        # bottom right
        pattern(ax,n-1,right_x,lower_y,size/2) 
    
# Comment the other figures except the one you want to view
plt.close("all") 
fig, ax = plt.subplots()
pattern(ax,4,0,0,400)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('squaresa.png')


#pattern(ax,3,0,0,400)
#ax.set_aspect(1.0)
#ax.axis('off')
#plt.show()
#fig.savefig('squaresb.png')

#pattern(ax,4,0,0,400)
#ax.set_aspect(1.0)
#ax.axis('off')
#plt.show()
#fig.savefig('squaresc.png')
