from classic.Particle import Particle
from random import random
from random import uniform
from random import randint


class GlobalSwarm():

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

    def __init__(self, function, dimensions, bounds,
                 swarm_size, max_iter, inertia_w, cognitive_c1, social_c2):

        error_gbest = -1
        gbest = []

        swarm = self.initialize_swarm(bounds, dimensions, swarm_size)

        i = 0
        while i < max_iter:

            #print("EVALUATE ERROR")
            for j in range(0, swarm_size):
                swarm[j].evaluate(function)
                #print("p: %s -> %s -> error: %s" % (j, swarm[j].position, swarm[j].error))

                if swarm[j].error < error_gbest or error_gbest == -1:
                    gbest = list(swarm[j].position)
                    error_gbest = float(swarm[j].error)

            #print("UPDATE VELOCITY AND POSITION")
            for j in range(0, swarm_size):
                swarm[j].update_velocity(gbest, dimensions, inertia_w, cognitive_c1, social_c2)
                swarm[j].update_position(bounds, dimensions)
                #print("p: %s, pos ->%s\n-> vel:%s" % (j, swarm[j].position, swarm[j].velocity))

            i += 1

            #print("ITERATION: %s" % i)
            #print("gBest: %s - error: %s" % (gbest, error_gbest))

        print("gBest Model - >>> gBest: %s - error: %s" % (gbest, error_gbest))
