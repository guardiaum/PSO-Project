import matplotlib.pyplot as plt

class PlotData(object):

    @staticmethod
    def convergence_iteration_plot(algorithms, final, function_name, bounds, minimum):
        lines = []
        names = []
        markers = ['o', '8', 's', '*', 'p']
        for i in range(0, len(algorithms)):

            x = []
            y = []
            label = ''
            marker = ''
            for j in range(0, len(final)):

                for key, value in final[j].items():
                    if algorithms[i] == key:
                        if key not in names:
                            label = key
                            marker = markers[i]
                            names.append(key)
                            x.append(value[0])
                            y.append(value[1])
                        elif key in names:
                            x.append(value[0])
                            y.append(value[1])

            print('a: ', algorithms[i])
            print('x: ', x)
            print('y: ', y)
            line, = plt.plot(x, y, label=label, marker=marker)
            lines.append(line)
        plt.suptitle("Convergence plot over max iterations for Function: %s" % function_name)
        plt.title("Bounds: %s, Global Minimum: %s" % (bounds, minimum), fontdict={'fontsize': 8})
        plt.xlabel('max iterations')
        plt.ylabel('convergence point')
        plt.legend(lines, names)
        plt.savefig("plots/" + function_name + "_convergence_iterations_plot.png", bbox_inches='tight')
        plt.gcf().clear()
        plt.cla()
        plt.clf()
        plt.close()