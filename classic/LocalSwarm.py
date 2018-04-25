from classic.Particle import Particle
from util.Neighborhood import Neighborhood
from random import random
from random import uniform
from random import randint

class LocalSwarm():

    def initialize_swarm(self, bounds, dimensions, swarm_size):
        swarm = []

        #print("INITIAL POSITIONING")

        lower_bound = bounds[0][0]
        upper_bound = bounds[0][1]

        for i in range(0, swarm_size):

            p0 = []
            v0 = []
            for dim in range(0, dimensions):
                p0.append(uniform(lower_bound, upper_bound))
                v0.append(random())

            swarm.append(Particle(p0, v0))
            #print("p: %s -> %s" % (i, swarm[i].position))

        return swarm

    def __init__(self, function, dimensions, bounds, n_size,
                 swarm_size, max_iter, inertia_w, cognitive_c1, social_c2):

        error_gbest = -1
        gbest = []
        lbests = [None] * swarm_size

        swarm = self.initialize_swarm(bounds, dimensions, swarm_size)

        iter = 0
        while iter < max_iter:

            for i in range(swarm_size):
                swarm[i].evaluate(function)

                # saves best particle as global best
                if swarm[i].error < error_gbest or error_gbest == -1:
                    gbest = list(swarm[i].position)
                    error_gbest = float(swarm[i].error)

            # Find lbest for each particle
            for i in range(swarm_size):
                # selection of neighborhood
                # static/dynamic
                # static -> only list indexes
                # dynamic -> euclidian distance
                '''
                neighbors = Neighborhood.get_dynamic(swarm[i], n_size, swarm)
                '''
                neighbors = Neighborhood.get_static(i, n_size, swarm_size)

                lbest = swarm[i]
                for n in range(len(neighbors)):
                    n_index = neighbors[n]

                    if lbest.error_best < swarm[n_index].error_best:
                        lbest = swarm[n_index]

                lbests[i] = lbest

            # update position and velocity for each particle according to its lbest
            for i in range(swarm_size):
                lbest = lbests[i].position
                swarm[i].update_velocity(lbest, dimensions, inertia_w, cognitive_c1, social_c2)
                swarm[i].update_position(bounds, dimensions)

            iter += 1

            #print("ITERATION: %s" % iter)
            #print("gBest: %s - error: %s" % (gbest, error_gbest))

        print("lBest Model - >>> gBest: %s - error: %s" % (gbest, error_gbest))