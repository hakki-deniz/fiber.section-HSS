###
# This piece of code defines the function to create square HSS Section
# The help of the reference study for OpenSeesPy makes this code possible.
#
#  ##   Reference used for guidance:
#
#       OpenSeesPy: Python library for the OpenSees finite element framework
#       Minjie Zhu, Frank McKenna, Michael H.Scott
#       https://doi.org/10.1016/j.softx.2017.10.009
#
###

###
# Input Variables

    # secID = section ID (#)
    # matID = material ID (#)
    # matTorsion = material ID for torsion (#)
    # H = depth of section (mm)
    # h = depth of flat wall (mm)
    # B = depth of section (mm)
    # b = depth of flat wall (mm)
    # t  = wall thickness (mm)
    # Comment : For square HSS; H = B and h = b
    # nsubdiv_y = number of fibers along depth that goes along local y axis
    # nsubdiv_z = number of fibers along depth that goes along local z and circle axis
    
###

import openseespy.opensees as ops

def HSSsection3D(secID, matID, matTorsion, H, h, B, b, t, nsubdiv_y, nsubdiv_z):

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
              
    secTag = secID + 1000
          
    # Calculate Torsional Stiffness (for 3D Model)
    E = 200000.0;                               # Elasticity modulus of steel material
    nu_ = 0.3                                   # Poisson ratio for steel
    G_  = (E/2.0*(1+nu_));                      # Shear modulus
    do_ = h;                                    # Depth of flat wall (median depth)
    J_ = (do_**3)*t;                            # Torsional constant
    GJ_ = G_*J_;                                # Torsional stiffness

    # Create Square HSS Section    
    ops.section("Fiber", secID)
    #                matTag numSubdivCirc numSubdivRad yCenter zCenter intRad extRad startAng endAng
    ops.patch("circ",matID,nsubdiv_z,nsubdiv_y,y1,z2,r,R,90.0,180.0)
    ops.patch("circ",matID,nsubdiv_z,nsubdiv_y,y2,z2,r,R,0.0,90.0)
    ops.patch("circ",matID,nsubdiv_z,nsubdiv_y,y1,z1,r,R,180.0,270.0)
    ops.patch("circ",matID,nsubdiv_z,nsubdiv_y,y2,z1,r,R,270.0,360.0)
            
    #              matTag numSubdiv_y numSubdiv_z yI zI yJ zJ
    ops.patch("rect",matID,nsubdiv_z,nsubdiv_y,y1,z3,y2,z5)
    ops.patch("rect",matID,nsubdiv_y,nsubdiv_z,y3,z1,y5,z2)
    ops.patch("rect",matID,nsubdiv_y,nsubdiv_z,y6,z1,y4,z2)
    ops.patch("rect",matID,nsubdiv_z,nsubdiv_y,y1,z6,y2,z4)
         
    # Assign Torsional Stiffness (for 3D Model) with Section Aggregator
    ops.uniaxialMaterial("Elastic",matTorsion,GJ_);                     # Define material for torsional stiffness
    ops.section("Aggregator",secTag,matTorsion,"T","-section",secID);   # Aggregate sections
