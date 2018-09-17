import numpy as np
import numpy.random as rng
import time

medium_mtx = np.array( rng.rand( 2000, 2000 ))
medium_vec = np.array( rng.rand( 2000, 1 ))

t0 = time.time()
y_s = np.matmul( np.linalg.inv( medium_mtx ), medium_vec )
t1 = time.time()
print( 'slow time: {} '.format( t1 - t0 ))



t0_f = time.time()
y_f = np.linalg.solve( medium_mtx, medium_vec )
t1_f = time.time()
print( 'fast time: {} '.format( t1_f - t0_f ))
