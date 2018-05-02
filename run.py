from classic.GlobalSwarm import *
from ring.LocalSwarm import *
from lips.LIPSSwarm import *
from fips.FIPSSwarm import *
from util.BenchmarkFunctions import BenchmarkFunctions as Functions
from evaluation.Evaluation import *
from evaluation.PlotData import *

# sets optimization function
func = Functions.booth

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

# inform for plotting
function_name = 'Booth'
minimum = global_minimum
bounds = bounds1

# run
final = []

algorithms = ['classic', 'ring', 'ring2', 'fips']

# iterations
for max_iter in range(200, 2200, 200):
    print("max iteration: ", max_iter)

    # Initialize Optimization Algorithms
    classic = GlobalSwarm(function=func, bounds=bounds, swarm_size=50, max_iter=max_iter)
    ring = LocalSwarm(function=func, bounds=bounds, n_size=2, swarm_size=50, max_iter=max_iter)
    ring2 = LocalSwarm(function=func, bounds=bounds, n_size=6, swarm_size=50, max_iter=max_iter)
    fips = FIPSSwarm(function=func, bounds=bounds, swarm_size=50, nsize=2, max_iter=max_iter)
    # lips = LIPSSwarm(function=func, bounds=bounds, swarm_size=50, nsize=2, max_iter=max_iter)

    classic_errors = []
    ring_errors = []
    ring2_errors = []
    fips_errors = []
    lips_errors = []

    # repetitions
    for r in range(50):
        classic_errors.append(classic.main())
        ring_errors.append(ring.main())
        ring2_errors.append(ring2.main())
        fips_errors.append(fips.main())

    classic_avg = Evaluation.error_average(classic_errors)
    ring_avg = Evaluation.error_average(ring_errors)
    ring2_avg = Evaluation.error_average(ring2_errors)
    fips_avg = Evaluation.error_average(fips_errors)

    final.append({'classic': [max_iter, classic_avg]})
    final.append({'ring': [max_iter, ring_avg]})
    final.append({'ring2': [max_iter, ring2_avg]})
    final.append({'fips': [max_iter, fips_avg]})

print("PLOTTING...")

PlotData.convergence_iteration_plot(algorithms, final, function_name, bounds, minimum)

