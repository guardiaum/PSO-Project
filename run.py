from classic.GlobalSwarm import *
from classic.LocalSwarm import *
from util.BenchmarkFunctions import BenchmarkFunctions as Functions

# sets optimization function
func = Functions.sphere

# Select bounds according to function
# Any bounds ->> sphere, rosenbrock

# booth, matyas, levi_13
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
GlobalSwarm(function=func, dimensions=2, bounds=bounds1,
            swarm_size=20, max_iter=1000,
            inertia_w=0.5, cognitive_c1=0.5, social_c2=0.5)

LocalSwarm(function=func, dimensions=2, bounds=bounds1,
           n_size=2, swarm_size=20, max_iter=1000,
           inertia_w=0.5, cognitive_c1=0.5, social_c2=0.5)