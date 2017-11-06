import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle


class HyperPipes2DPlot:

    def __init__(self, data_x, data_y):
        self.y_unique_values, self.y_unique_indices = np.unique(
            data_y, return_inverse=True)
        self.n_y_unique = self.y_unique_values.shape[0]
        self.points = data_x
        self.target = data_y
        self.colors = ['b', 'g', 'c', 'm', 'k', 'y']
        self.figure = plt.figure()

    def __getVisualHyperPipe__(self, x, y, color):
        min_x, max_x = min(x), max(x)
        min_y, max_y = min(y), max(y)
        return Rectangle((min_x, min_y), (max_x - min_x), (max_y - min_y), fill=None, alpha=1, edgecolor=color)

    def plot(self):
        currentAxis = plt.gca()

        for i in range(self.n_y_unique):
            target_class = self.y_unique_values[i]
            target_class_indices = np.where(self.target == target_class)
            points_filtered = self.points[target_class_indices]

            x = points_filtered[:, 0]
            y = points_filtered[:, 1]
            rect = self.__getVisualHyperPipe__(x, y, self.colors[i])
            currentAxis.add_patch(rect)
            class_plot, = plt.plot(
                x, y, self.colors[i] + 's', label="Class " + str(i + 1))

        plt.title('HyperPipes Model')
        plt.ylabel('Y Axis')
        plt.xlabel('X Axis')
        plt.legend()
        plt.show()

    def add_plot_point(self, point):
        plt.plot(point[0], point[1], 'rs', label="Validation")
