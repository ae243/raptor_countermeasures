import constants
import sys
import numpy
import matplotlib.pyplot as plt

data = constants.data1
mean1 = numpy.mean(data.values())
std1 = numpy.std(data.values())
print "2008"
print "Mean: " + str(mean1)
print "Std Dev: " + str(std1)

data2 = constants.data2
mean2 = numpy.mean(data2.values())
std2 = numpy.std(data2.values())
print "2009"
print "Mean: " + str(mean2)
print "Std Dev: " + str(std2)

data3 = constants.data3
mean3 = numpy.mean(data3.values())
std3 = numpy.std(data3.values())
print "2010"
print "Mean: " + str(mean3)
print "Std Dev: " + str(std3)

data4 = constants.data4
mean4 = numpy.mean(data4.values())
std4 = numpy.std(data4.values())
print "2011"
print "Mean: " + str(mean4)
print "Std Dev: " + str(std4)

data5 = constants.data5
mean5 = numpy.mean(data5.values())
std5 = numpy.std(data5.values())
print "2012"
print "Mean: " + str(mean5)
print "Std Dev: " + str(std5)

data6 = constants.data6
mean6 = numpy.mean(data6.values())
std6 = numpy.std(data6.values())
print "2013"
print "Mean: " + str(mean6)
print "Std Dev: " + str(std6)

data7 = constants.data7
mean7 = numpy.mean(data7.values())
std7 = numpy.std(data7.values())
print "2014"
print "Mean: " + str(mean7)
print "Std Dev: " + str(std7)

data8 = constants.data8
mean8 = numpy.mean(data8.values())
std8 = numpy.std(data8.values())
print "2015"
print "Mean: " + str(mean8)
print "Std Dev: " + str(std8)

data9 = constants.data9
mean9 = numpy.mean(data9.values())
std9 = numpy.std(data9.values())
print "2016"
print "Mean: " + str(mean9)
print "Std Dev: " + str(std9)

labels = ['2008','2009','2010','2011','2012','2013','2014','2015','2016']
x = [1,2,3,4,5,6,7,8,9]
y = [.433,.454,.468,.470,.472,.488,.476,.470,.485]

yerr = [std1,std2, std3, std4, std5, std6, std7, std8, std9]
plt.figure()
plt.errorbar(x, y, yerr=yerr, fmt='o-')
plt.xticks(x,labels,size='small')
plt.axis([0, 10, 0, 1])
plt.xlabel('Year')
plt.ylabel('Average Tor AS Resilience')
plt.title('AS Hijack Resilience Trend')
plt.show()
