import numpy as np


class HyperPipe:

    def __init__(self):
        self.n_dimensions = 0
        self.numerical_bounds = []

    def fit(self, data_x, data_y):
        data_y_unique = data_y.unique()

        if(data_y_unique.shape[0] > 1):
            raise ValueError(
                'A different target class was added to the HyperPipe', data_y_unique)

        self.target_class = data_y_unique[0]
        self.n_dimensions = data_x.shape[1]

        # Initializes bounds
        for i in range(self.n_dimensions):
            self.numerical_bounds[i] = []
            self.numerical_bounds[i][0] = float('+inf')  # lower bound 1
            self.numerical_bounds[i][1] = float('-inf')  # upper bound 9

        # Add instances
        for i in range(data_x.shape[0]):
            self.__add_instance__(data_x[i])

        return None

    def __add_instance__(self, data_x):
        #check boundaries
        for i in range(self.n_dimensions):
            if(data_x[i] < self.numerical_bounds[i][0]):
                self.numerical_bounds[i][0] = data_x[i]
            if(data_x[i] > self.numerical_bounds[i][1]):
                self.numerical_bounds[i][1] = data_x[i]

        return None

    def partial_contains(self, data_x):
        count = 0
        for i in range(self.n_dimensions):
            if(data_x[i] > self.numerical_bounds[i][0] and data_x[i] < self.numerical_bounds[i][1]):
                count += 1

        return (count, self.target_class)


class HyperPipes:

    def __init__(self):
        self.hyper_pipes = []

    def fit(self, data_x, data_y):
        self.y_unique_values, self.y_unique_indices = np.unique(
            data_y, return_inverse=True)
        self.n_y_unique = self.y_unique_values.shape[0]
        self.hyper_pipes = [HyperPipe() for i in self.n_y_unique]

        for i in range(self.n_y_unique):
            target_class = data_y[i]
            target_class_indices = np.where(data_y == data_y[i])
            data_x_filtered = data_x[target_class_indices]
            self.hyper_pipes[i].fit(data_x_filtered, target_class)

        return None

    def predict(self, data_x):
        scores = []
        for i in range(self.n_y_unique):
            scores.append(self.hyper_pipes[i].partial_contains(data_x))

        return scores


class Instance:
    def __init__(self, data, target):
        self.data = data
        self.target = target
