class HyperPipe:

    def __init__(self, points):
        self.n_dimensions = len(points)
        self.min_max_dimensions = self.__GetMinMaxDimensions__(self.n_dimensions, points)

    def __GetMinMaxDimensions__(self, n_dimensions, points):
        min_max_dimensions = []
        for i in range(n_dimensions):
            d = points[i]
            min_d, max_d = min(d), max(d)
            min_max_dimensions.append([min_d, max_d])
        return min_max_dimensions

    def Classify(self, point):
        for i in range(self.n_dimensions):
            if(point[i] < self.min_max_dimensions[i][0] or point[i] > self.min_max_dimensions[i][1]):
                return False
        return True
