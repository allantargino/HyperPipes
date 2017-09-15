from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle

# def getVisualHyperPipe(x, y, color):
#     min_x, max_x = min(x), max(x)
#     min_y, max_y = min(y), max(y)
#     return Rectangle((min_x, min_y), (max_x - min_x), (max_y - min_y), fill=None, alpha=1, edgecolor=color)

points =    [
                [
                    [0.5, 0.7, 0.5, 1.0, 2.5, 1.7],
                    [0.5, 1.0, 1.0, 0.7, 0.2, 0.9]
                ],
                [
                    [2.5, 2.3, 2.0, 2.6, 1.7],
                    [2.5, 2.0, 3.0, 2.5, 3.3]
                ]
            ]

hyperPipes = []


def GetMinMaxXY(x, y):
    min_x, max_x = min(x), max(x)
    min_y, max_y = min(y), max(y)
    return min_x, max_x, min_y, max_y


def BuildHyperPipe(min_x, max_x, min_y, max_y):
    def HyperPipe(x, y):
        if(x >= min_x and x <= max_x and y >= min_y and y <= max_y):
            return True
        return False
    return HyperPipe



for i in range(2):
    x,y = points[i][0], points[i][1]
    min_x, max_x, min_y, max_y = GetMinMaxXY(x,y)
    hyperPipe = BuildHyperPipe(min_x, max_x, min_y, max_y)
    hyperPipes.append(hyperPipe)

x=0.6
y=0.7

for i, hyperPipe in enumerate(hyperPipes):
    print hyperPipe(x,y)

# rect1 = getVisualHyperPipe(x1, y1, 'b')
# rect2 = getVisualHyperPipe(x2, y2, 'g')

# plt.figure()
# currentAxis = plt.gca()
# currentAxis.add_patch(rect1)
# currentAxis.add_patch(rect2)
# plt.plot(x1, y1, 'bs', x2, y2, 'gs')
# plt.title('HyperPipes Model Example')
# plt.ylabel('Y Axis')
# plt.xlabel('X Axis')
# plt.show()
