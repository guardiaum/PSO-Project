from classic.GlobalSwarm import *
from ring.LocalSwarm import *
from fips.FIPSSwarm import *
from lips.LIPSSwarm import *
from evaluation.Evaluation import *
from evaluation.PlotData import *


def niche_pso(func, bounds, n_size, max_iter):
    lips = LIPSSwarm(function=func, bounds=bounds, swarm_size=50, nsize=n_size, max_iter=max_iter)
    lips.main();


def repetitions(func, function_name, bounds,  minimum):
    final = []
    algorithms = ['classic', 'ring_2n', 'ring_6n', 'fips', 'wfips', 'wdfips']

    # iterations
    for max_iter in range(100, 2100, 100):
        print("max iteration: ", max_iter)

        # Initialize Optimization Algorithms
        classic = GlobalSwarm(function=func, bounds=bounds, swarm_size=10, max_iter=max_iter)
        ring = LocalSwarm(function=func, bounds=bounds, n_size=2, swarm_size=10, max_iter=max_iter)
        ring2 = LocalSwarm(function=func, bounds=bounds, n_size=6, swarm_size=10, max_iter=max_iter)
        fips = FIPSSwarm(function=func, bounds=bounds, swarm_size=10, nsize=2, w_type='static', max_iter=max_iter)
        wfips = FIPSSwarm(function=func, bounds=bounds, swarm_size=10, nsize=2, w_type='fitness', max_iter=max_iter)
        wdfips = FIPSSwarm(function=func, bounds=bounds, swarm_size=10, nsize=2, w_type='distance', max_iter=max_iter)

        classic_errors = []
        ring_errors = []
        ring2_errors = []
        fips_errors = []
        wfips_errors = []
        wdfips_errors = []

        # repetitions
        for r in range(20):
            classic_gbest, classic_gbests = classic.main()
            classic_errors.append(classic_gbest)
            ring_gbest, ring_gbests = ring.main()
            ring_errors.append(ring_gbest)
            ring2_gbest, ring2_gbests = ring2.main()
            ring2_errors.append(ring2_gbest)
            fips_gbest, fips_gbests = fips.main()
            fips_errors.append(fips_gbest)
            wfips_gbest, wfips_gbests = wfips.main()
            wfips_errors.append(wfips_gbest)
            wdfips_gbest, wdfips_gbests = wdfips.main()
            wdfips_errors.append(wdfips_gbest)

        classic_avg = Evaluation.error_average(classic_errors)
        ring_avg = Evaluation.error_average(ring_errors)
        ring2_avg = Evaluation.error_average(ring2_errors)
        fips_avg = Evaluation.error_average(fips_errors)
        wfips_avg = Evaluation.error_average(wfips_errors)
        wdfips_avg = Evaluation.error_average(wdfips_errors)

        final.append({'classic': [max_iter, classic_avg]})
        final.append({'ring_2n': [max_iter, ring_avg]})
        final.append({'ring_6n': [max_iter, ring2_avg]})
        final.append({'fips': [max_iter, fips_avg]})
        final.append({'wfips': [max_iter, wfips_avg]})
        final.append({'wdfips': [max_iter, wdfips_avg]})

    print("PLOTTING...")

    PlotData.convergence_iteration_plot(algorithms, final, function_name, bounds, minimum)


def no_repetitions(max_iter, func, function_name, bounds, minimum):
    # Initialize Optimization Algorithms
    classic = GlobalSwarm(function=func, bounds=bounds, swarm_size=10, max_iter=max_iter)
    ring = LocalSwarm(function=func, bounds=bounds, n_size=2, swarm_size=10, max_iter=max_iter)
    ring2 = LocalSwarm(function=func, bounds=bounds, n_size=6, swarm_size=10, max_iter=max_iter)
    fips = FIPSSwarm(function=func, bounds=bounds, swarm_size=10, nsize=2, w_type='static', max_iter=max_iter)
    wfips = FIPSSwarm(function=func, bounds=bounds, swarm_size=10, nsize=2, w_type='fitness', max_iter=max_iter)
    wdfips = FIPSSwarm(function=func, bounds=bounds, swarm_size=10, nsize=2, w_type='distance', max_iter=max_iter)

    classic_gbest, classic_gbests = classic.main()
    ring_gbest, ring_gbests = ring.main()
    ring2_gbest, ring2_gbests = ring2.main()
    fips_gbest, fips_gbests = fips.main()
    wfips_gbest, wfips_gbests = wfips.main()
    wdfips_gbest, wdfips_gbests = wdfips.main()

    data = {'classic': classic_gbests,
            'ring_2n': ring_gbests,
            'ring_6n': ring2_gbests,
            'fips': fips_gbests,
            'wfips': wfips_gbests,
            'wdfips': wdfips_gbests}

    print("PLOTTING...")
    PlotData.convergence_plot(data, function_name, bounds, minimum)
