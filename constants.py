# physical constants for tov solver

import math

ln10 = log(10.0)
pi = math.pi
twopi = 2.0*pi
threepi = 3.0*pi
fourpi = 4.0*pi
threepisquare = (3.0*pi**2)

# physical and astronomical constants, in cgs units
boltzmann = 1.3806488e-16
avogadro = 6.02214129e23 
clight = 2.99792458e10
clight2	= clight**2
sigma_SB = 5.670400e-5
arad = sigma_SB*4.0/clight
amu = 1.660538921e-24
hbar = 1.054571726e-27
finestructure = 7.2973525698e-3
Gnewton	= 6.67384e-8
Mneutron = 1.674927351e-24
Mproton	= 1.672621777e-24
si_charge = 1.602176565e-19
electroncharge = si_charge*clight*0.1
Melectron = 9.10938291e-28
Mmuon = 1.883531475e-25
theta_weak = 0.2223

# astronomical constants -- see http://ssd.jpl.nasa.gov/?constants
julian_day = 86400
julian_year = 365.25 * julian_day
GMsun = 1.32712440018e26
Msun = GMsun/Gnewton

# some conversion factors
mev_to_ergs = 1.602176565e-6
fm_to_cm = 1.0e-13
ergs_to_mev = 1.0/mev_to_ergs
cm_to_fm = 1.0/fm_to_cm
	
# atomic units (length in Bohr radii for hydrogen, energy in Rydberg)
a_Bohr = hbar**2/Melectron/electroncharge**2
Rydberg	= 0.5*electroncharge**2/a_Bohr
	
# nuclear units (c = 1, hbar = 197 MeV fm; energy is expressed in MeV, length in fm)
hbarc_n = hbar*clight/mev_to_ergs/fm_to_cm
mass_n = mev_to_ergs/clight2
length_n = fm_to_cm
density_n = 1.0/fm_to_cm**3
pressure_n = mev_to_ergs*density_n
temperature_n = mev_to_ergs/boltzmann
Mn_n = Mneutron*clight2*ergs_to_mev
Mp_n = Mproton*clight2*ergs_to_mev
Me_n = Melectron*clight2*ergs_to_mev
amu_n = amu*clight2*ergs_to_mev
	
# gravitational units (G = c = 1; unit of mass is Msun)
mass_g = Msun
potential_g = clight2
length_g = Gnewton*mass_g/potential_g
density_g = mass_g/length_g**3
pressure_g = density_g*potential_g
time_g = length_g/clight