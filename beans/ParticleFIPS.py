from beans.Particle import Particle
from util.Neighborhood import Neighborhood
from random import uniform


class ParticleFIPS(Particle):

    def __init__(self, p0, v0):
        Particle.__init__(self, p0, v0)
        self.neighbors = []
        self.n_size = len(self.neighbors)

    def get_neighbors(self, target, n_size, swarm):
        indexes = Neighborhood.get_static(target, n_size, len(swarm))

        # print("NEIGHBORS", indexes)
        self.neighbors = []
        for i in range(len(indexes)):
            self.neighbors.append(swarm[indexes[i]])

        self.n_size = len(self.neighbors)

    def update_velocity(self, inertia_w, dimensions):
        phi = self.calculate_phi()
        p = self.calculate_p(phi, dimensions)

        phi_ = 0
        for i in range(0, len(phi)):
            phi_ *= phi[i]

        for d in range(0, dimensions):
            self.velocity[d] = inertia_w * (self.velocity[d] + phi_ * (p[d] - self.position[d]))

    def calculate_p(self, phi, dimensions):
        p = []
        numerator = 0
        divisor = 0

        for k in range(0, len(self.neighbors)):
            for d in range(dimensions):
                k_fitness = self.neighbors[k].error_best
                numerator += k_fitness * phi[k] * self.neighbors[k].pbest[d]
                divisor += k_fitness * phi[k]

            p.append(numerator / divisor)

        return p

    def calculate_phi(self):

        phi_limit = 4.1 / self.n_size
        phi = []

        x = uniform(0, phi_limit)

        for i in range(0, self.n_size):
            phi.append(x)

        return phi
