from classic.GlobalSwarm import *
from ring.LocalSwarm import *
from lips.LIPSSwarm import *
from fips.FIPSSwarm import *
from util.BenchmarkFunctions import BenchmarkFunctions as Functions
from evaluation.Evaluation import *

# sets optimization function
func = Functions.holder_table

# Select bounds according to function
# Any bounds ->> sphere, rosenbrock

# booth, matyas, levi_13, cross_in_tray, holder_table
bounds1 = [(-10, 10), (-10, 10)]
# ackley, himmelblaus, three_hump_camel
bounds2 = [(-5, 5), (-5, 5)]
# rastringin
bounds3 = [(-5.12, 5.12), (-5.12, 5.12)]
# beale
bounds4 = [(-4.5, 4.5), (-4.5, 4.5)]
# goldstein_price
bounds5 = [(-2, 2), (-2, 2)]
# bukin_6
bounds5 = [(-15, 3), (-5, 3)]

# Initialize Optimization Algorithms

classic = GlobalSwarm(function=func, bounds=bounds1, swarm_size=50, max_iter=300)
classic.main()

ring = LocalSwarm(function=func, bounds=bounds1, n_size=2, swarm_size=50, max_iter=300)
ring.main()

ring2 = LocalSwarm(function=func, bounds=bounds1, n_size=6, swarm_size=50, max_iter=300)
ring2.main()

fips = FIPSSwarm(function=func, bounds=bounds1, swarm_size=50, nsize=2, max_iter=300)
fips.main()

lips = LIPSSwarm(function=func, bounds=bounds1, swarm_size=50, nsize=2, max_iter=300)
lips.main()

'''
# run
classic_errors = []
ring_errors = []
ring2_errors = []

for i in range(20):
    print("Execution %s" % i)
    classic_errors.append(classic.main())
    ring_errors.append(ring.main())
    ring2_errors.append(ring2.main())

print(Evaluation.error_average(classic_errors))
print(Evaluation.error_average(ring_errors))
print(Evaluation.error_average(ring2_errors))
'''