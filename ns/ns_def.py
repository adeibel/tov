import numpy as np

class ns:
    
    def __init__(self):

		# basic variables
		self.n_interior_pts = np.empty(0)
        self.mass = np.empty(0)
        self.baryonic_mass = np.empty(0)
        self.radius = np.empty(0)
        self.grav_potential = np.empty(0)
        self.inertia = np.empty(0)
        
        # thermal variables 
        self.temp = np.empty(0)
        self.luminosity = np.empty(0)
        self.specific_heat = np.empty(0)
        
        
	def _tov_eqns(self):

        tolerance_in_r = 1.0e-4 
        tolerance_in_p = 1.0e-4
        
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

