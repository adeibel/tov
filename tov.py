	# tov solver for a tabulated EOS

	import matplotlib.pyplot
	import numpy 
	import constants 

	# controls
	rtol = 1.0e-6
	atol = 1.0e-7

	core_step = 1.0e4	! cm
	crust_step = 0.05	! variation in lnP
	
	# boundary conditions
	T_ePhi = 0.01
	P_start = 160.0
	P_end = 1.0e-6
	Phi_start = 0.0
