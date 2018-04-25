import math

class Neighborhood():

    def euclidian_dist(particle1, particle2):
        distance = 0

        for i in range(len(particle1.position) - 1):
            distance += (particle1.position[i] - particle2.position[i]) ** 2

        return math.sqrt(distance)

    def get_static(target_index, n_size, swarm_size):
        neighbors = []
        range_by_side = n_size // 2

        for i in range(1, range_by_side + 1):
            previous = target_index - i
            next = target_index + i

            if next >= swarm_size:
                next = -1 + i

            neighbors.append(previous)
            neighbors.append(next)

        return neighbors


    def get_dynamic(target, n_size, swarm):

        distances = []

        for i in range(len(swarm)):
            distance = Neighborhood.euclidian_dist(target, swarm[i])
            distances.append([i, distance])

        def use_distance(temp):
            return temp[1]

        distances = sorted(distances, key=use_distance)

        neighbors = []
        for i in range(n_size):
            neighbors.append(distances[i][0])

        return neighbors