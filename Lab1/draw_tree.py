# Course: 2302-001
# Author: Esteban Retana
# Assignment: Create figures or fractals based on the knowledge of recursion
# Instructor: Olac Fuentes
# TA: Eduardo Lara
# Date of last modification:2/8/19
# Purpose: Practice recursion by creating fractals

import numpy as np
import matplotlib.pyplot as plt
import time

def draw_tree(ax,n,x_shift,y_shift,x,y):
    if n>0:
        q = np.array([[x,y],[x-x_shift,y-y_shift]])
        q1 = np.array([[x,y],[x+x_shift,y-y_shift]])
        ax.plot(q[:,0],q[:,1],color='k')
        ax.plot(q1[:,0],q1[:,1],color='k')
        
        draw_tree(ax,n-1,x_shift/2,y_shift,x-x_shift,y-y_shift)
        draw_tree(ax,n-1,x_shift/2,y_shift,x+x_shift,y-y_shift)
        
# Comment the other figures except the one you want to view
start_time = time.time()
plt.close("all")
fig, ax = plt.subplots()
draw_tree(ax,4,20,10,0,0)
ax.set_aspect(1.0)
ax.axis('on')
plt.show()
fig.savefig('treea.png')

#draw_tree(ax,4,20,10,0,0)
#ax.set_aspect(1.0)
#ax.axis('on')
#plt.show()
#fig.savefig('treeb.png')

# 7 is the max
#draw_tree(ax,7,20,10,0,0)
#ax.set_aspect(1.0)
#ax.axis('on')
#plt.show()
#fig.savefig('treec.png')
end_time = time.time() - start_time
print(end_time)