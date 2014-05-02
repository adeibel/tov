	# tov solver for a tabulated EOS

	import matplotlib.pyplot
	import numpy 
	import constants 
	import star_library

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

	tov_startup(datadir,ierr)
	#if (ierr /= 0) stop
	
	star_handle = alloc_tov_handle(ierr)
	#if (ierr /= 0) stop
	
	star_library.tov_set_microphysics(star_handle,sf_gaps,micro_ipar,micro_rpar,ierr)
	sf_scale = 0.0
	star_library.tov_set_integration(star_handle,rtol,atol,.false.,core_step,crust_step,ipar,rpar,ierr)

	star_library.tov_solve(star_handle,P_start, Phi_start,P_end,T_ePhi,y, ipar, rpar, ierr)
	y = 0.0
	star_library.tov_set_integration(star_handle,rtol,atol,.true.,core_step,crust_step,ipar,rpar,ierr)
	star_library.tov_integrate(star_handle,P_start,Phi_start,P_end,T_ePhi,y,ipar,rpar,ierr)

	star_library.tov_shutdown()