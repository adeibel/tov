from numpy import empty, array, loadtxt
import scipy.interpolate as si

class eos:
    
    def __init__(self,fname=None, use_builtin=None,skiprows=0,
     usecols=None):
        
        if fname is not None:
            try:
                self.rho,self.epsilon,self.pressure =
                 loadtxt(fname,usecols=usecols,skiprows=skiprows,unpack=True)
            except:
                print "something went wrong"
                self.rho = empty(0)
                self.epsilon = empty(0)
                self.pressure = empty(0)
                pass
        elif use_builtin is not None:
            if use_builtin='Steiner':
                self.rho,self.epsilon,self.pressure = loadSteiner()
            else:
                print 'warning: ',use_builtin,' is not a valid builtin'
                self.rho = empty(0)
                self.epsilon = empty(0)
                self.pressure = empty(0)
        else:
            print 'warning: eos is not initialized'
            self.rho = empty(0)
            self.epsilon = empty(0)
            self.pressure = empty(0)
