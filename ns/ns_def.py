import numpy as np

class ns:
    
    def __init__(self):

		self.n_interior_pts = np.empty(0)
        self.mass = np.empty(0)
        self.baryonic_mass = np.empty(0)
        self.radius = np.empty(0)
        self.grav_potential = np.empty(0)
        self.inertia = np.empty(0)
        
	def _tov_eqns(self):

	

