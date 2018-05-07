import math


class BenchmarkFunctions(object):

    # global minimum
    # f(0,0)=0
    # -5.12 <= x,y <= 5.12
    @staticmethod
    def rastringin(position):
        total = 0
        for i in range(len(position)):
            total += position[i]**2 - 10 * math.cos(2 * math.pi * position[i])
        return 10 * len(position) + total


    # global minimum
    # f(0,0)=0
    # -5 <= x,y <= 5
    @staticmethod
    def ackley(position):
        x = position[0]
        y = position[1]

        part1 = math.sqrt(0.5 * (x ** 2 + y ** 2))
        part2 = math.cos(2 * math.pi * x) + math.cos(2 * math.pi * y)
        return -20 * math.exp(-0.2 * part1) - math.exp(0.5 * part2) + math.e + 20


    # global minimum
    # f(0, ..., 0) = 0
    # -inf <= xi <= inf
    @staticmethod
    def sphere(position):
        total = 0

        for i in range(len(position)):
            total += position[i] ** 2

        return total


    # global minimum
    # f(0, ..., 0) = 0
    # -inf <= xi <= inf
    @staticmethod
    def rosenbrock(position):
        total = 0
        for i in range(len(position)-1):
            total += 100 * (position[i+1] - position[i]**2)**2 + (1 + position[i])**2

        return total

    # global minimum
    # f(x*) = 0 -> x* = (0, ..., 0)
    # -600 <= xi <= 600
    @staticmethod
    def griewank(position):
        a = 0
        for i in range(1, len(position)+1):
            a += (position[i-1]**2)/4000

        b = 0
        for i in range(1, len(position)+1):
            b *= math.cos(position[i-1]/math.sqrt(i)) + 1

        return a - b

    # Global minimum
    # f(x*) = 0 -> x* = 0
    # -100 <= xi <= 100
    @staticmethod
    def schaffer_n6(position):
        x = position[0]
        y = position[1]

        a = math.sin(math.sqrt(x**2 + y**2)) - 0.5
        b = (1 + 0.001 * (x**2 + y**2))**2

        return 0.5 + (a/b)

    # global minimum
    # f(3,0.5)=0
    # -4.5 <= x, y <= 4.5
    @staticmethod
    def beale(position):
        x = position[0]
        y = position[1]

        return (1.5 - x + x * y)**2 + (2.25 - x + x*y**2)**2 + (2.625 - x + x*y**3)**2


    # global minimum
    # f(0,-1)=3
    # -2 <= x, y <= 2
    @staticmethod
    def goldstein_price(position):
        x = position[0]
        y = position[1]

        first = 1 + (x + y + 1)**2 * (19 - 14*x + 3*x**2 - 14*y + 6*x*y + 3*y**2)
        scnd = 30 + (2*x - 3*y)**2 * (18 - 32*x + 12*x**2 + 48*y - 36*x*y + 27*y**2)
        return first * scnd


    # global minimum
    # f(1,3)=0
    # -10 <= x,y <= 10
    @staticmethod
    def booth(position):
        x = position[0]
        y = position[1]
        return (x + 2*y - 7) ** 2 + (2*x + y - 5) ** 2


    # global minimum
    # f(-10,1)=0
    # -15 <= x <= -5
    # -3 <= y <= 3
    @staticmethod
    def bukin_6(position):
        x = position[0]
        y = position[1]
        return 100 * math.sqrt(math.fabs(y - 0.01 * x ** 2)) + 0.01 * math.fabs(x + 10)


    # global minimum
    # f(0,0)=0
    # -10 <= x, y <= 10
    @staticmethod
    def matyas(position):
        x = position[0]
        y = position[1]
        return 0.26 * (x**2 + y**2) - 0.48 * x * y


    # global minimum
    # f(1,1)=0
    # -10 <= x, y <= 10
    @staticmethod
    def levi_13(position):
        x = position[0]
        y = position[1]

        first = math.sin(3 * math.pi * x) ** 2 + (x - 1) ** 2
        scnd = (1 + math.sin(3 * math.pi * y)) + (y - 1) ** 2 * (1 + math.sin(2 * math.pi * y))

        return first * scnd


    # global minimum
    # f(3.0,2.0)=0
    # f(-2.805118, 3.131312)=0.0
    # f(-3.779310, -3.283186)=0.0
    # f(3.584428, -1.848126)=0.0
    # -5 <= x, y <= 5
    @staticmethod
    def himmelblaus(position):
        x = position[0]
        y = position[1]
        return (x**2 + y - 11)**2 + (x + y**2 - 7)**2


    # global minimum
    # f(0,0)=0
    # -5 <= x, y <= 5
    @staticmethod
    def three_hump_camel(position):
        x = position[0]
        y = position[1]
        return (2 * x**2) - (1.05 * x**4) + ((x**6)/6) + x * y + y**2

    # global minimum
    # f(1.34941, -1.34941) = -2.06261
    # f(1.34941, 1.34941) = -2.06261
    # f(-1.34941, 1.34941) = -2.06261
    # f(-1.34941, -1.34941) = -2.06261
    # -10 <= x,y <= 10
    @staticmethod
    def cross_in_tray(position):
        x = position[0]
        y = position[1]

        a = math.exp(math.fabs(100 - (math.sqrt(x**2 + y**2) / math.pi)))
        b = math.fabs(math.sin(x) * math.sin(y) * a) + 1

        return -0.0001 * (b**0.1)

    # global minimum
    # f(8.05502, 9.66459) = -19.2085
    # f(-8.05502, 9.66459) = -19.2085
    # f(8.05502, -9.66459) = -19.2085
    # f(-8.05502, -9.66459) = -19.2085
    # -10 <= x,y <= 10
    @staticmethod
    def holder_table(position):
        x = position[0]
        y = position[1]

        a = math.exp(math.fabs(1 - (math.sqrt(x**2 + y**2) / math.pi)))
        return -math.fabs(math.sin(x) * math.cos(y) * a)