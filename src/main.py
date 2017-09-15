from hyperPipes import HyperPipe
from plot import HyperPipesPlot

points = [
    [  # class_1
        [0.5, 0.7, 0.5, 1.0, 2.5, 1.7],
        [0.5, 1.0, 1.0, 0.7, 0.2, 0.9]
    ],
    [  # class_2
        [2.5, 2.3, 2.0, 2.6, 1.7],
        [2.5, 2.0, 3.0, 2.5, 3.3]
    ]
]

point = [2.1, 2.3]

for i in range(len(points)):
    class_i = points[i]
    hyperPipe = HyperPipe(class_i)
    print('Class ' + str(i) + ': ' + str(hyperPipe.Classify(point)))

hp_plt = HyperPipesPlot(points)
hp_plt.add_plot_point(point)
hp_plt.plot()
