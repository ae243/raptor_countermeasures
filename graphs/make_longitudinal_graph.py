import sys
import numpy
import matplotlib.pyplot as plt

labels = ['2008','2009','2010','2011','2012','2013','2014','2015','2016']
y = [.433,.454,.468,.470,.472,.488,.476,.470,.485]
x = [1,2,3,4,5,6,7,8,9]
plt.plot(x, y, '-', markersize=20)
plt.xticks(x,labels,size='small')
plt.xlabel('Year')
plt.ylabel('Average Tor AS Resilience')
plt.title('AS Hijack Resilience Trend')
plt.show()
