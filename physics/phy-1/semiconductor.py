# Copyright 2023 Donglin Qiu

import matplotlib.pyplot as plt
import numpy as np

name = '半导体电阻'
y_name = '电阻R/Ω'
x_name = '温度t/K'
t = np.array([36.8,40.1,41.7,42.8,44.5]) + 273.15
R = np.array([1689,1479,1379,1319,1279])
fit = np.polyfit(1/t,np.log(R),1)
k = 1.38064852e-23

plt.xlabel(x_name)
plt.ylabel(y_name)
plt.rcParams['font.sans-serif']=['SimHei']

R0 = np.exp(fit[1])
E = fit[0]*k
e_k = fit[0]
#plt.plot(t,fit[0]*t+fit[1])
for i in np.arange(t[0]-1,t[-1]+1,0.05):
    plt.plot(i,R0*np.exp(e_k/i),'r.',markersize=0.5)
plt.plot(t,R,'^')
for i in range(len(t)): plt.text(t[i],R[i],'(%.1f,%d)'%(t[i],R[i]))
res = '%s\nR0 = %.5EΩ  E = %.5EJ/K'%(name,R0,E)
plt.title(res)
plt.grid(True)

plt.savefig('phy-1-2.png', dpi=300)
plt.show()
