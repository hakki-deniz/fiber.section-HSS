###
# This piece of code use the pre-defined function codes to
# visualise the created square-HSS section.
#
# The help of the reference study for OpenSeesPy makes this code possible.
#
#  ##   Reference used for guidance:
#
#       OpenSeesPy: Python library for the OpenSees finite element framework
#       Minjie Zhu, Frank McKenna, Michael H.Scott
#       https://doi.org/10.1016/j.softx.2017.10.009
#
###

import openseespy.opensees as ops
import openseespy.postprocessing.ops_vis as opsv
import matplotlib.pyplot as plt

ops.wipe()
ops.model('basic', '-ndm', 2, '-ndf', 3)  # frame 2D

## Values for an Example
B = 102
H = 102
h = 66
b = 66
t = 6.4

nsubdivz,nsubdivy = 4,2

r = B/2 - (b/2+t)
R= r + t
    
y1 = -b/2
y2 = b/2
y3 = -B/2
y4 = B/2
y5 = -B/2+t
y6 = B/2-t
  
z1 = -h/2
z2 = h/2
z3 = H/2-t
z4 = -H/2+t
z5 = H/2
z6 = -H/2

matID = 1          
ops.uniaxialMaterial("Steel02", matID, 460, 200000, 0.01, 20, 0.925, 0.15)

fib_sec_ = [['section', 'Fiber'],
             ["patch", "circ",matID,nsubdivz,nsubdivy,y1,z2,r,R,90.0,180.0],
             ["patch", "circ",matID,nsubdivz,nsubdivy,y2,z2,r,R,0.0,90.0],
             ["patch", "circ",matID,nsubdivz,nsubdivy,y1,z1,r,R,180.0,270.0],
             ["patch", "circ",matID,nsubdivz,nsubdivy,y2,z1,r,R,270.0,360.0],
             ['patch', "rect",matID,nsubdivz,nsubdivy,y1,z3,y2,z5],
             ['patch', "rect",matID,nsubdivy,nsubdivz,y3,z1,y5,z2],
             ['patch', "rect",matID,nsubdivy,nsubdivz,y6,z1,y4,z2],
             ['patch', "rect",matID,nsubdivz,nsubdivy,y1,z6,y2,z4]]
    
            
matcolor = ['grey', 'lightgrey', 'gold', 'w', 'w', 'w']
opsv.plot_fiber_section(fib_sec_, matcolor=matcolor)
plt.axis('equal')
plt.show()
