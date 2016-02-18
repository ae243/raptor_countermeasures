import sys
import numpy
import matplotlib.pyplot as plt

y = [0,2.63, 4.29, 4.29, 4.29, 5.96, 9.90]
x = [.004, .005, .006, .007, .008, .009, .01]
plt.plot(x, y, '-', markersize=20)
plt.xticks(x,size='small')
plt.xlabel('Threshold Value')
plt.ylabel('False Positive Percentage')
plt.title('False Positive Rate in Relation to Frequency Heuristic Threshold Values')
plt.show()
