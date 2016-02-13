import sys
import matplotlib.pyplot as plt

labels = ['200429', '39138', '20773', '57858', '31863', '44869', '58073', '24961', '197540', '198310', '31042', '50673', '50923', '12874', '49544']
y = [0.0, .24, .28, .39, .42, .44, .45, .45, .51, .56, .57, .62, .68, .72, .76]
x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

plt.plot(x, y, '.', markersize=20)
plt.xticks(x,labels,size='small')
plt.xlabel('ASN')
plt.xticks(rotation='vertical')
plt.ylabel('Hijack Resilience')
plt.title('Hijack Resilience for Tor-related ASNs that Were Affected by the Indosat 2014 Hijack')
plt.show()
