	# subroutines for tov solver

	import numpy 
	import constants 

	def tov_startup(datadir_root,ierr):
		ierr = 0
		if (tov_is_initialized) return
		tov_def_init(datadir_root)
		tov_is_initialized = TRUE

	def tov_shutdown():
		do i = 1, max_tov_handles
			call do_free_tov(i)
		end do
		tov_is_initialized = FALSE
		
		