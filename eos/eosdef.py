import numpy as np
import scipy.interpolate as si

class eos:
    
    def __init__(self,fname=None, use_builtin=None,skiprows=0,
     usecols=None):

        self.rho = np.empty(0)
        self.epsilon = np.empty(0)
        self.pressure = np.empty(0)
        
        if fname is not None:
                 _load_eos_from_file(fname,skiprows=skiprows,usecols=usecols)
        elif use_builtin is not None:
            if use_builtin == 'SLB':
                self._load_steiner()
            else:
                print 'warning: ',use_builtin,' is not a valid builtin'
        else:
            print 'warning: eos is not initialized'


    def _load_eos_from_file(self,fname,skiprows=0,usecols=None):
        self.rho,self.epsilon,self.pressure = \
            np.loadtxt(fname,skiprows=skiprows,usecols=usecols)

    def _load_steiner(self):
        Nrows = 53
        raw_data = """\
1.572094e-01  1.500000e+02  2.150000e+00 
1.829538e-01  1.750000e+02  3.813432e+00 
2.084989e-01  2.000000e+02  5.760000e+00 
2.338196e-01  2.250000e+02  8.152204e+00 
2.588934e-01  2.500000e+02  1.067000e+01 
2.837009e-01  2.750000e+02  1.306650e+01 
3.082257e-01  3.000000e+02  1.587000e+01 
3.324540e-01  3.250000e+02  1.965803e+01 
3.563746e-01  3.500000e+02  2.443000e+01 
3.799790e-01  3.750000e+02  2.997262e+01 
4.032605e-01  4.000000e+02  3.580000e+01 
4.262148e-01  4.250000e+02  4.173525e+01 
4.488389e-01  4.500000e+02  4.911000e+01 
4.711319e-01  4.750000e+02  5.897515e+01 
4.930939e-01  5.000000e+02  6.975000e+01 
5.147262e-01  5.250000e+02  7.979042e+01 
5.360312e-01  5.500000e+02  8.983000e+01 
5.570122e-01  5.750000e+02  1.012319e+02 
5.776732e-01  6.000000e+02  1.155000e+02 
5.980188e-01  6.250000e+02  1.330369e+02 
6.180540e-01  6.500000e+02  1.497000e+02 
6.377842e-01  6.750000e+02  1.619493e+02 
6.572153e-01  7.000000e+02  1.732000e+02 
6.763533e-01  7.250000e+02  1.873533e+02 
6.952043e-01  7.500000e+02  2.033000e+02 
7.137745e-01  7.750000e+02  2.188750e+02 
7.320704e-01  8.000000e+02  2.327000e+02 
7.500984e-01  8.250000e+02  2.440592e+02 
7.678647e-01  8.500000e+02  2.541000e+02 
7.853757e-01  8.750000e+02  2.645258e+02 
8.026378e-01  9.000000e+02  2.774000e+02 
8.196570e-01  9.250000e+02  2.937375e+02 
8.364395e-01  9.500000e+02  3.100000e+02 
8.529912e-01  9.750000e+02  3.230866e+02 
8.693180e-01  1.000000e+03  3.362000e+02 
8.854258e-01  1.025000e+03  3.529036e+02 
9.013199e-01  1.050000e+03  3.719000e+02 
9.170060e-01  1.075000e+03  3.916365e+02 
9.324894e-01  1.100000e+03  4.144000e+02 
9.477751e-01  1.125000e+03  4.404629e+02 
9.628684e-01  1.150000e+03  4.582000e+02 
9.777740e-01  1.175000e+03  4.589371e+02 
9.924967e-01  1.200000e+03  4.577000e+02 
1.007041e+00  1.225000e+03  4.705888e+02 
1.021412e+00  1.250000e+03  4.943000e+02 
1.035613e+00  1.275000e+03  5.217827e+02 
1.049649e+00  1.300000e+03  5.504000e+02 
1.063524e+00  1.325000e+03  5.784929e+02 
1.077242e+00  1.350000e+03  6.039000e+02 
1.104221e+00  1.400000e+03  6.423922e+02 
1.130617e+00  1.450000e+03  6.720000e+02 
1.156455e+00  1.500000e+03  7.017193e+02 
1.181762e+00  1.550000e+03  7.325000e+02
        """
        
        self.rho = np.zeros(Nrows)
        self.epsilon = np.zeros(Nrows)
        self.pressure = np.zeros(Nrows)
        
        for row, indx in zip(raw_data.split('\n'),range(Nrows)):
            tok = row.split()
            print indx,tok
            self.rho[indx] = float(tok[0])
            self.epsilon[indx] = float(tok[1])
            self.pressure[indx] = float(tok[2])
