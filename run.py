from classic.GlobalSwarm import *
from ring.LocalSwarm import *
from lips.LIPSSwarm import *
from fips.FIPSSwarm import *
from util.BenchmarkFunctions import BenchmarkFunctions as Functions
from evaluation.Evaluation import *
from evaluation.PlotData import *


def run_repetitions(func, function_name, bounds,  minimum):
    final = []
    algorithms = ['classic', 'ring_2n', 'ring_6n', 'fips']

    # iterations
    for max_iter in range(200, 2200, 200):
        print("max iteration: ", max_iter)

        # Initialize Optimization Algorithms
        classic = GlobalSwarm(function=func, bounds=bounds, swarm_size=10, max_iter=max_iter)
        ring = LocalSwarm(function=func, bounds=bounds, n_size=2, swarm_size=10, max_iter=max_iter)
        ring2 = LocalSwarm(function=func, bounds=bounds, n_size=6, swarm_size=10, max_iter=max_iter)
        fips = FIPSSwarm(function=func, bounds=bounds, swarm_size=10, nsize=2, max_iter=max_iter)
        # lips = LIPSSwarm(function=func, bounds=bounds, swarm_size=50, nsize=2, max_iter=max_iter)

        classic_errors = []
        ring_errors = []
        ring2_errors = []
        fips_errors = []

        # repetitions
        for r in range(50):
            classic_gbest, classic_gbests = classic.main()
            classic_errors.append(classic_gbest)
            ring_gbest, ring_gbests = ring.main()
            ring_errors.append(ring_gbest)
            ring2_gbest, ring2_gbests = ring2.main()
            ring2_errors.append(ring2_gbest)
            fips_gbest, fips_gbests = fips.main()
            fips_errors.append(fips_gbest)

        classic_avg = Evaluation.error_average(classic_errors)
        ring_avg = Evaluation.error_average(ring_errors)
        ring2_avg = Evaluation.error_average(ring2_errors)
        fips_avg = Evaluation.error_average(fips_errors)

        final.append({'classic': [max_iter, classic_avg]})
        final.append({'ring_2n': [max_iter, ring_avg]})
        final.append({'ring_6n': [max_iter, ring2_avg]})
        final.append({'fips': [max_iter, fips_avg]})

    print("PLOTTING...")

    PlotData.convergence_iteration_plot(algorithms, final, function_name, bounds, minimum)


def run_no_repetitions(max_iter, func, function_name, bounds, minimum):
    # Initialize Optimization Algorithms
    classic = GlobalSwarm(function=func, bounds=bounds, swarm_size=10, max_iter=max_iter)
    ring = LocalSwarm(function=func, bounds=bounds, n_size=2, swarm_size=10, max_iter=max_iter)
    ring2 = LocalSwarm(function=func, bounds=bounds, n_size=6, swarm_size=10, max_iter=max_iter)
    fips = FIPSSwarm(function=func, bounds=bounds, swarm_size=10, nsize=2, max_iter=max_iter)

    classic_gbest, classic_gbests = classic.main()
    ring_gbest, ring_gbests = ring.main()
    ring2_gbest, ring2_gbests = ring2.main()
    fips_gbest, fips_gbests = fips.main()

    data = {'classic': classic_gbests,
            'ring_2n': ring_gbests,
            'ring_6n': ring2_gbests,
            'fips': fips_gbests}

    print("PLOTTING...")
    PlotData.convergence_plot(data, function_name, bounds, minimum)

# Select bounds according to function
# Any bounds ->> sphere, rosenbrock
# booth, matyas, levi_13, cross_in_tray, holder_table
bounds1 = [(-10, 10), (-10, 10)]
# ackley, himmelblaus, three_hump_camel
bounds2 = [(-5, 5), (-5, 5)]
# rastringin
rastringin_bounds = [(-5.12, 5.12), (-5.12, 5.12)]
# beale
beale_bounds = [(-4.5, 4.5), (-4.5, 4.5)]
# goldstein_price
goldstein_bounds = [(-2, 2), (-2, 2)]
# bukin_6
bukin_bounds = [(-15, 3), (-5, 3)]

# special global minimum
global_minimum = 0.0  # other functions
goldstein_minimum = 3
cross_in_tray_minimum = -2.06261
holder_table_minimum = -19.2085

functions_name = ["Rastringin", "Ackley", "Sphere", "Rosenbrock", "Beale",
                  "Goldstein_price", "Booth", "Buking_N6", "Matyas", "Levi_N13",
                  "Three_hump_camel"]
functions = [Functions.rastringin, Functions.ackley, Functions.sphere,
             Functions.rosenbrock, Functions.beale, Functions.goldstein_price,
             Functions.booth, Functions.bukin_6, Functions.matyas, Functions.levi_13,
             Functions.three_hump_camel]
minimus = [global_minimum, global_minimum, global_minimum, global_minimum,
           global_minimum, goldstein_minimum, global_minimum, global_minimum, global_minimum,
           global_minimum, global_minimum]
bounds_ = [rastringin_bounds, bounds2, bounds1, bounds1, beale_bounds, goldstein_bounds, bounds1,
           bukin_bounds, bounds1, bounds1, bounds2]

for i in range(0, len(functions_name)):
    run_repetitions(functions[i], functions_name[i], bounds_[i], minimus[i])
    # run_no_repetitions(20, functions[i], functions_name[i], bounds_[i], minimus[i])