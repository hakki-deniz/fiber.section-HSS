###
# This piece of code defines the function to create square HSS Section
    # The help of the reference study for OpenSeesPy makes this code possible.
    #
    #  ##   Reference used for guidance:
    #
    #       OpenSeesPy: Python library for the OpenSees finite element framework
    #       Minjie Zhu, Frank McKenna, Michael H.Scott
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

# To use this function in your analysis, call it as given in the following:

	from fib_sec_HSS import*

	HSSsection3D(secID, matID, matTorsion, H, h, B, b, t, nsubdiv_y, nsubdiv_z)


	# You can visualise your HSS-section by using the **section_plot.py** file with proper inputs.

# Reference:	

	Zhu, M., McKenna, F., & Scott, M. H. (2018). Openseespy: Python library for the opensees finite element framework. SoftwareX, 7, 6-11. 
	https://doi.org/10.1016/j.softx.2017.10.009
