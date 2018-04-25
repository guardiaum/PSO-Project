from Particle import Particle
from BenchmarkFunctions import BenchmarkFunctions as Functions


class Swarm():

    def __init__(self, function, dimensions, bounds,
                 swarm_size, max_iter, inertia_w, cognitive_c1, social_c2):

        error_gbest = -1
        gbest = []

        swarm = []
        print("INITIAL POSITIONING")

        for i in range(0, swarm_size):
            swarm.append(Particle(dimensions))
            print("p: %s -> %s" % (i, swarm[i].position))

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

            print("ITERATION: %s" % i)
            print("gBest: %s - error: %s" % (gbest, error_gbest))

        print("END >>> gBest: %s - error: %s" % (gbest, error_gbest))


func = Functions.goldstein_price
Swarm(function=func, dimensions=2, bounds=[(-2, 2), (-2, 2)],
      swarm_size=100, max_iter=10000,
      inertia_w=0.5, cognitive_c1=0.5, social_c2=0.5)