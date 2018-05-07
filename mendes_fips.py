from util.BenchmarkFunctions import BenchmarkFunctions as Functions
from util.run import *

'''
    EXPERIMENTS REPRODUTION FOR
    The Fully Informed Particle Swarm: Simpler, Maybe Better
    Rui Mendes, James Kennedy and José Neves
'''

# functions bounds
sphere_bounds = [(-100, 100)] * 30  # sphere
rosenbrock_bounds = [(-30, 30)] * 30  # rosenbrock
rastringin_bounds = [(-5.12, 5.12)] * 30  # rastringin
griewank_bounds_10d = [(-600, 600)] * 10  # Griewank 10 dimensions
griewank_bounds_30d = [(-600, 600)] * 30  # Griewank 30 dimensions
schaffer_bounds = [(-100, 100), (-100, 100)]  # Schaffer N6

# minimum global
global_minimum = 0.0

# functions
functions_name = ["Rastringin", "Sphere", "Rosenbrock",
                  "Griewank_10d", "Griewank_30d", "Schaffer_n6"]

# initialize execution parameters
functions = [Functions.rastringin, Functions.sphere, Functions.rosenbrock,
             Functions.griewank, Functions.griewank, Functions.schaffer_n6]
minimus = [global_minimum, global_minimum, global_minimum,
           global_minimum, global_minimum, global_minimum]
bounds_ = [rastringin_bounds, sphere_bounds, rosenbrock_bounds,
           griewank_bounds_10d, griewank_bounds_30d, schaffer_bounds]

# execution
for i in range(0, len(functions)):
    print(functions_name[i])
    repetitions(functions[i], functions_name[i], bounds_[i], minimus[i])
    # no_repetitions(1000, functions[i], functions_name[i], bounds_[i], minimus[i])