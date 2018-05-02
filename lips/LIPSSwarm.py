from beans.ParticleLIPS import ParticleLIPS
from random import uniform


class LIPSSwarm(object):

    def __init__(self, function, bounds, swarm_size, nsize, max_iter,
                 inertia_w=0.7298):
        self.function = function
        self.bounds = bounds
        self.dimensions = len(bounds)
        self.swarm_size = swarm_size
        self.nsize = nsize
        self.max_iter = max_iter
        self.inertia_w = inertia_w

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

        '''
        print("\nLIPS Model")
        for i in range(0, len(swarm)):
            if swarm[i].error_best < 1 and swarm[i].error_best not in error_best:
                gbest.append(swarm[i].position)
                error_best.append(swarm[i].error_best)

        for i in range(0, len(gbest)):
            print("P: %s > %s -> %s" % (i, gbest[i], error_best[i]))
        '''
        return error_best
