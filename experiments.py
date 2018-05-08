from util.BenchmarkFunctions import BenchmarkFunctions as Functions
from util.run import *

''' Tests with 2 dimensions '''

'''
    UNIMODAL EXPERIMENTS
'''
def unimodal():
    # Select bounds according to function
    bounds1 = [(-10, 10)] * 30  # booth, matyas, levi_13, cross_in_tray, holder_table
    bounds2 = [(-5, 5)] * 30  # ackley, himmelblaus, three_hump_camel
    sphere_bounds = [(-100, 100)] * 30  # sphere
    rosenbrock_bounds = [(-30, 30)] * 30  # rosenbrock
    griewank_bounds = [(-600, 600)] * 30  # Griewank
    schaffer_bounds = [(-100, 100)] * 30  # Schaffer N6
    rastringin_bounds = [(-5.12, 5.12)] * 30  # rastringin
    beale_bounds = [(-4.5, 4.5)] * 30  # beale
    goldstein_bounds = [(-2, 2)] * 30  # goldstein_price
    bukin_bounds = [(-15, 3)] * 30  # bukin_6

    # special global minimum
    global_minimum = 0.0  # other functions
    goldstein_minimum = 3

    functions_name = ["Rastringin", "Sphere", "Rosenbrock", "Ackley", "Beale",
                      "Goldstein_price", "Booth", "Buking_N6", "Matyas", "Levi_N13",
                      "Three_hump_camel", "Griewank", "Schaffer_n6"]

    functions = [Functions.rastringin, Functions.sphere, Functions.rosenbrock,
                 Functions.ackley, Functions.beale, Functions.goldstein_price,
                 Functions.booth, Functions.bukin_6, Functions.matyas, Functions.levi_13,
                 Functions.three_hump_camel, Functions.griewank, Functions.schaffer_n6]

    minimus = [global_minimum, global_minimum, global_minimum, global_minimum,
               global_minimum, goldstein_minimum, global_minimum, global_minimum, global_minimum,
               global_minimum, global_minimum, global_minimum, global_minimum]

    bounds_ = [rastringin_bounds, sphere_bounds, rosenbrock_bounds, bounds2,
               beale_bounds, goldstein_bounds, bounds1,
               bukin_bounds, bounds1, bounds1, bounds2, griewank_bounds, schaffer_bounds]

    for i in range(0, len(functions_name)):
        print(functions_name[i])
        # repetitions(functions[i], functions_name[i], bounds_[i], minimus[i])
        no_repetitions(1000, functions[i], functions_name[i], bounds_[i], minimus[i])


'''
    MULTIMODAL EXPERIMENTS
'''
def multimodal():
    cross_in_tray_bounds = [(-10, 10)] * 2 # cross_in_tray
    holder_table_bounds = [(-10, 10)]  * 2# holder_table
    himmelblaus_bounds = [(-5, 5)] * 2 # himmelblaus

    # f(1.34941, -1.34941) = -2.06261
    # f(1.34941, 1.34941) = -2.06261
    # f(-1.34941, 1.34941) = -2.06261
    # f(-1.34941, -1.34941) = -2.06261
    cross_in_tray_minimum = [-2.06261] * 4  # 4

    # f(8.05502, 9.66459) = -19.2085
    # f(-8.05502, 9.66459) = -19.2085
    # f(8.05502, -9.66459) = -19.2085
    # f(-8.05502, -9.66459) = -19.2085
    holder_table_minimum = [-19.2085] * 4  # 4

    # f(3.0,2.0)=0
    # f(-2.805118, 3.131312)=0.0
    # f(-3.779310, -3.283186)=0.0
    # f(3.584428, -1.848126)=0.0
    himmelblaus_minimum = [0.0] * 4  # 4

    functions = [Functions.cross_in_tray, Functions.holder_table, Functions.himmelblaus]
    functions_name = ['cross_in_tray', 'holder_table', 'himmelblaus']
    functions_bounds = [cross_in_tray_bounds, holder_table_bounds, himmelblaus_bounds]
    functions_minimus = [cross_in_tray_minimum, holder_table_minimum, himmelblaus_minimum]

    for i in range(len(functions_name)):
        print(functions_name[i])
        niche_pso(functions[i], functions_bounds[i], functions_minimus[i], 0.005, 3, 20000)
        print("")


multimodal()
# unimodal()