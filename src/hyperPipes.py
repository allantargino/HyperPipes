from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle


def getVisualHyperPipe(x, y, color):
    min_x, max_x = min(x), max(x)
    min_y, max_y = min(y), max(y)
    return Rectangle((min_x, min_y), (max_x - min_x), (max_y - min_y), fill=None, alpha=1, edgecolor=color)


x1 = [0.5, 0.7, 0.5, 1.0, 2.5, 1.7]
y1 = [0.5, 1.0, 1.0, 0.7, 0.2, 0.9]

x2 = [2.5, 2.3, 2.0, 2.6, 1.7]
y2 = [2.5, 2.0, 3.0, 2.5, 3.3]

rect1 = getVisualHyperPipe(x1, y1, 'b')
rect2 = getVisualHyperPipe(x2, y2, 'g')

plt.figure()
currentAxis = plt.gca()
currentAxis.add_patch(rect1)
currentAxis.add_patch(rect2)
plt.plot(x1, y1, 'bs', x2, y2, 'gs')
plt.title('HyperPipes Model Example')
plt.ylabel('Y Axis')
plt.xlabel('X Axis')
plt.show()
