import numpy as np

class ns:
    
    def __init__(self):

		# basic variables
        self.pressure = np.empty(0)
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
        
        
	def tov_eqns(self):

        tov_set_integration()
        self.pressure = P_start
        self.grav_potential = Phi_start
        self.temp = T_ePhi


def tov_set_integration():
    
    # controls
    rtol = 1.0e-6
    atol = 1.0e-7

    # for rootfind
    tolerance_in_r = 1.0e-4
    tolerance_in_p = 1.0e-4
    
    # step sizes
    core_step = 1.0e4	# cm
    crust_step = 0.05	# variation in lnP
	
    # boundary conditions
    T_ePhi = 0.01
    P_start = 160.0
    P_end = 1.0e-6
    Phi_start = 0.0

def tov_set_microphysics(rtol,atol,output_grid,core_step,crust_step,ipar,rpar,ierr):
    """ need to set following routines
        core neutrino
        crust neutrino
        core eos
        crust eos"""