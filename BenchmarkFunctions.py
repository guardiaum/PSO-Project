import math


class BenchmarkFunctions(object):

    # global minimum
    # f(0, ..., 0) = 0
    # -inf <= xi <= inf
    def sphere(position):
        total = 0

        for i in range(len(position)):
            total += position[i] ** 2

        return total


    # global minimum
    # f(1,3)=0
    # -10 <= x,y <= 10
    def booth(position):
        x = position[0]
        y = position[1]
        return (x + 2*y - 7) ** 2 + (2*x + y - 5) ** 2



    # global minimum
    # f(0,0)=0
    # -10 <= x, y <= 10
    def matyas(position):
        x = position[0]
        y = position[1]
        return 0.26 * (x**2 + y**2) - 0.48 * x * y


    # global minimum
    # f(0,0)=0
    # -5 <= x, y <= 5
    def three_hump_camel(position):
        x = position[0]
        y = position[1]
        return (2 * x**2) - (1.05 * x**4) + ((x**6)/6) + x * y + y**2


    # global minimum
    # f(3.0,2.0)=0
    # f(-2.805118, 3.131312)=0.0
    # f(-3.779310, -3.283186)=0.0
    # f(3.584428, -1.848126)=0.0
    # -5 <= x, y <= 5
    def himmelblaus(position):
        x = position[0]
        y = position[1]
        return (x**2 + y - 11)**2 + (x + y**2 - y)**2


    # global minimum
    # f(1,1)=0
    # -10 <= x, y <= 10
    def levi(position):
        x = position[0]
        y = position[1]

        first = math.sin(3 * math.pi * x) ** 2 + (x - 1) ** 2
        scnd = (1 + math.sin(3 * math.pi * y)) + (y - 1) ** 2 * (1 + math.sin(2 * math.pi * y))

        return first * scnd


    # global minimum
    # f(-10,1)=0
    # -15 <= x <= -5
    # -3 <= y <= 3
    def bukin(position):
        x = position[0]
        y = position[1]
        return 100 * math.sqrt(math.fabs( y - 0.01 * x**2)) + 0.01 * math.fabs(x + 10)


    # global minimum
    # f(0,-1)=3
    # -2 <= x, y <= 2
    def goldstein_price(position):
        x = position[0]
        y = position[1]

        first = 1 + (x + y + 1)**2 * (19 - 14*x + 3*x**2 - 14*y + 6*x*y + 3*y**2)
        scnd = 30 + (2*x - 3*y)**2 * (18 - 32*x + 12*x**2 + 48*y - 36*x*y + 27*y**2)
        return first * scnd