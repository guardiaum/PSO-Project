from util.BenchmarkFunctions import BenchmarkFunctions as Functions
from util.run import *

''' Tests with 2 dimensions '''

# Select bounds according to function
bounds1 = [(-10, 10), (-10, 10)]  # booth, matyas, levi_13, cross_in_tray, holder_table
bounds2 = [(-5, 5), (-5, 5)]  # ackley, himmelblaus, three_hump_camel
sphere_bounds = [(-100, 100), (-100, 100)]  # sphere
rosenbrock_bounds = [(-30, 30), (-30, 30)]  # rosenbrock
griewank_bounds = [(-600, 600), (-600, 600)]  # Griewank 10 dimensions
schaffer_bounds = [(-100, 100), (-100, 100)]  # Schaffer N6
rastringin_bounds = [(-5.12, 5.12), (-5.12, 5.12)]  # rastringin
beale_bounds = [(-4.5, 4.5), (-4.5, 4.5)]  # beale
goldstein_bounds = [(-2, 2), (-2, 2)]  # goldstein_price
bukin_bounds = [(-15, 3), (-5, 3)]  # bukin_6

# special global minimum
global_minimum = 0.0  # other functions
goldstein_minimum = 3
cross_in_tray_minimum = -2.06261
holder_table_minimum = -19.2085

functions_name = ["Rastringin", "Sphere", "Rosenbrock", "Ackley", "Beale",
                  "Goldstein_price", "Booth", "Buking_N6", "Matyas", "Levi_N13",
                  "Three_hump_camel"]

functions = [Functions.rastringin, Functions.sphere, Functions.rosenbrock,
             Functions.ackley, Functions.beale, Functions.goldstein_price,
             Functions.booth, Functions.bukin_6, Functions.matyas, Functions.levi_13,
             Functions.three_hump_camel]

minimus = [global_minimum, global_minimum, global_minimum, global_minimum,
           global_minimum, goldstein_minimum, global_minimum, global_minimum, global_minimum,
           global_minimum, global_minimum]

bounds_ = [rastringin_bounds, sphere_bounds, rosenbrock_bounds, bounds2,
           beale_bounds, goldstein_bounds, bounds1,
           bukin_bounds, bounds1, bounds1, bounds2]

'''

for i in range(0, len(functions_name)):
    print(functions_name[i])
    # run_repetitions(functions[i], functions_name[i], bounds_[i], minimus[i])
    no_repetitions(100, functions[i], functions_name[i], bounds_[i], minimus[i])

'''

'''
    MULTIMODAL EXPERIMENTS
'''

cross_in_tray_bounds = [(-10, 10)] * 2 # cross_in_tray
holder_table_bounds = [(-10, 10)]  * 2 # holder_table
himmelblaus_bounds = [(-5, 5)] * 2 # himmelblaus

cross_in_tray_minimum = -2.06261  # 4
holder_table_minimum = -19.2085  # 4
himmelblaus_minimum = 0.0  # 4

functions = [Functions.cross_in_tray, Functions.holder_table, Functions.himmelblaus]
functions_name = ['cross_in_tray', 'holder_table', 'himmelblaus']
functions_bounds = [cross_in_tray_bounds, holder_table_bounds, himmelblaus_bounds]

for i in range(len(functions_name)):
    print(functions_name[i])
    niche_pso(functions[i], functions_bounds[i], 2, 200)