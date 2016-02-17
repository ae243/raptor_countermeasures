import sys
import numpy
import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7]
y = [0,.44, 1.67, 2.02, 2.28, 2.28, 5.26]
labels = [.00000001, .0000001, .000001, .00001, .0001, .001, .01]
plt.plot(x, y, '-', markersize=20)
plt.xticks(x,labels,size='small')
plt.xlabel('Threshold Value')
plt.ylabel('False Positive Percentage')
plt.title('False Positive Rate in Relation to Time Heuristic Threshold Values')
plt.show()
