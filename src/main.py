from hyperPipe import HyperPipe

# points =    [
#                 [
#                     [0.5, 0.7, 0.5, 1.0, 2.5, 1.7],
#                     [0.5, 1.0, 1.0, 0.7, 0.2, 0.9]
#                 ],
#                 [
#                     [2.5, 2.3, 2.0, 2.6, 1.7],
#                     [2.5, 2.0, 3.0, 2.5, 3.3]
#                 ]
#             ]

points_class1 = [
    [0.5, 0.7, 0.5, 1.0, 2.5, 1.7],
    [0.5, 1.0, 1.0, 0.7, 0.2, 0.9],
    [0.5, 1.0, 1.0, 0.7, 0.2, 0.9]
]

hyperPipe = HyperPipe(points_class1)
print hyperPipe.Classify([0.6, 0.6, 0.6])

# for i in range(2):
#     x,y = points[i][0], points[i][1]
#     min_x, max_x, min_y, max_y = GetMinMaxXY(x,y)
#     hyperPipe = BuildHyperPipe(min_x, max_x, min_y, max_y)
#     hyperPipes.append(hyperPipe)

# x=0.6
# y=0.7

# for i, hyperPipe in enumerate(hyperPipes):
#     print hyperPipe(x,y)
