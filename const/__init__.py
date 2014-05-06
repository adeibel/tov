"""
=================
Constants
=================


physical and astronomical constants, in cgs units
=================================================

=================   ================================
"boltzmann"			Boltzmann constant
"avogadro" 			Avogadro constant
"clight" 			speed of light in vacuum
"clight2"			speed of light squared
"sigma_SB" 			Stefan-Boltzmann constant
"arad" 				radiation constant
"amu"				atomic mass unit
"hbar" 				reduced Planck's constant
"finestructure" 	fine structure constant 
"Gnewton"			Newtonian graviational constant
"Mneutron" 			mass of neutron
"Mproton"			mass of proton 
"si_charge" 		1.602176565e-19
"electroncharge" 	si_charge*clight*0.1
"Melectron" 		mass of electron
"Mmuon" 			mass of muon
"theta_weak"  		0.2223
=================   ================================

Astronomical constants
======================

========	=========================
"GMsun" 	Gnewton*Msun in cgs units
"Msun" 		solar mass in grams
========	========================="

Microscopic constants (nuclear units)
(c = 1, hbar = 197 MeV fm; energy is expressed in MeV, length in fm)
====================================================================

===============		========================
"hbarc_n"			reduced Planck's constant
"mass_n" 			conversion factor fromm grams to MeV
"length_n"      	conversion factor from cm to fm
"density_n" 		conversion factor from cm**-3 to fm**-3
"pressure_n"    	mev_to_ergs*density_n
"temperature_n" 	mev_to_ergs/boltzmann
"Mn_n" 				mass of neutron in MeV
"Mp_n" 				mass of proton in MeV
"Me_n" 				mass of electron in MeV
"amu_n" 			atomic mass unit in MeV
===============		========================

Macroscopic constants (gravitational units)
(G = c = 1; unit of mass is Msun)
====================================================================

=============	=======================================
"mass_g"		solar mass in grams
"potential_g"	clight2
"length_g" 		Gnewton*mass_g/potential_g
"density_g" 	mass_g/length_g**3
"pressure_g" 	density_g*potential_g
"time_g" 		length_g/clight
======================================================
"""

from const_def import *
