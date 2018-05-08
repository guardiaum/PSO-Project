from beans.ParticleLIPS import ParticleLIPS
from random import uniform
from math import fabs


class LIPSSwarm(object):

    def __init__(self, function, bounds, swarm_size, known_peeks, e, nsize, max_iter,
                 inertia_w=0.7298):
        self.function = function
        self.bounds = bounds
        self.dimensions = len(bounds)
        self.swarm_size = swarm_size
        self.nsize = nsize
        self.max_iter = max_iter
        self.inertia_w = inertia_w
        self.known_peeks = known_peeks[0]
        self.number_of_peeks = len(known_peeks)
        self.e = e

    @staticmethod
    def initialize_swarm(bounds, dimensions, swarm_size):
        swarm = []

        lower_bound = bounds[0][0]
        upper_bound = bounds[0][1]

        for i in range(0, swarm_size):

            p0 = []
            v0 = []
            for dim in range(0, dimensions):
                p0.append(uniform(lower_bound, upper_bound))
                v0.append(uniform(lower_bound, upper_bound))

            swarm.append(ParticleLIPS(p0, v0))
            # print("P: %s > %s - V: %s" % (i, swarm[i].position, swarm[i].velocity))

        return swarm

    def main(self):

        gbest = []
        error_best = []

        swarm = self.initialize_swarm(self.bounds, self.dimensions, self.swarm_size)

        for i in range(0, len(swarm)):
            swarm[i].evaluate(self.function)
            # print("P: %s > %s -> %s" % (i, swarm[i].pbest, swarm[i].error_best))

        iter = 0
        while iter < self.max_iter:

            for i in range(0, len(swarm)):
                swarm[i].get_neighbors(self.nsize, swarm)

                swarm[i].update_velocity(self.inertia_w, self.dimensions)

                swarm[i].update_position(self.bounds, self.dimensions)

                swarm[i].evaluate(self.function)

            iter += 1

        # stop criterium
        # if all particles have converged to some point bellow e
        # print("LIPS Model")
        for i in range(0, len(swarm)):
            print("P: %s > %s > %s" % (i, swarm[i].pbest ,swarm[i].error_best))
            if fabs(self.known_peeks - swarm[i].error_best) < self.e:
                error_best.append(swarm[i].error_best)

        for i in range(0, len(gbest)):
            print("P: %s > %s" % (i, error_best[i]))

        return error_best
