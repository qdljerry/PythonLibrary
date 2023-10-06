# Copyright 2023 Donglin Qiu

import matplotlib.pyplot as plt
import numpy as np

name = '铜导体电阻'
y_name = '电阻R/Ω'
x_name = '温度t/℃'
t = np.array([28.3,30.1,32.4,34.1,36.4])
R = np.array([58.59,58.97,59.44,59.84,60.35])
fit = np.polyfit(t,R,1)

plt.xlabel(x_name)
plt.ylabel(y_name)
plt.rcParams['font.sans-serif']=['SimHei']

plt.plot(t,fit[0]*t+fit[1])
plt.plot(t,R,'^')
for i in range(len(t)): plt.text(t[i],R[i],'(%.1f,%.2f)'%(t[i],R[i]))
res = '%s\nR0 = %.2fΩ, α= %.5E℃^-1'%(name,fit[1],fit[0]/fit[1])
plt.title(res)
plt.grid(True)

plt.savefig('copper.png', dpi=300)
plt.show()
