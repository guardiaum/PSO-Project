import numpy as np


class Evaluation(object):

    @staticmethod
    def error_average(errors):
        return np.mean(errors)