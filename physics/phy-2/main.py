import numpy as np
import matplotlib.pyplot as plt
import reportlab
from reportlab.pdfgen import canvas

# 等宽英文字体
plt.rcParams['font.sans-serif']=['SimHei','Times New Roman']

U1 = np.array([i*2.0 for i in range(11)])
I1 = np.array([0,3.9,7.8,11.7,15.7,19.6,23.6,27.6,31.7,35.7,39.9])
I2 = np.array([0,3.9,7.8,11.7,15.6,19.6,23.6,27.6,31.6,35.6,39.7])

U2 = np.array([0,.02,.04,.06,.08,.1,.15,.18,.2,.4,.6,1,1.5,2.5,3.5,4,4.5])
I3 = np.array([0,2.2,4.4,6.5,8.9,11.1,16,18.2,19.6,28.1,34.7,46.8,62.1,84.1,103.4,112.2,120.3])
R3 = U2/I3*1e3
R3[0] = R3[1]

U3 = np.array([0,.1,.3,.4,.5,.6,.65,.7,.72,.74,.76,.78])
I4 = np.array([0,0,0,0,.2,2.4,6.5,17.6,25.9,38.1,56.8,82.4])

# 1
title1 = '线性电阻的伏安特性'
xtitle1 = 'U (V)'
ytitle1 = 'I (mA)'

plt.subplot(1,2,1)
res = np.polyfit(U1,I1,1)
R1 = 1/res[0]*1e3
plt.plot(U1,U1*res[0]+res[1],label='拟合曲线')
plt.plot(U1,I1,'xr',label='内接法')
plt.title(title1 + '\nR = %.2fΩ'%R1)
plt.xlabel(xtitle1)
plt.ylabel(ytitle1)
plt.legend()
plt.grid(True)

plt.subplot(1,2,2)
res = np.polyfit(U1,I2,1)
R2 = 1/res[0]*1e3
plt.plot(U1,U1*res[0]+res[1],label='拟合曲线')
plt.plot(U1,I2,'xr',label='外接法')
plt.title(title1 + '\nR = %.2fΩ'%R2)
plt.xlabel(xtitle1)
plt.ylabel(ytitle1)
plt.legend()
plt.grid(True)

plt.savefig('1.png',dpi=250)
plt.close()

# 2
title2 = '非线性电阻(灯泡)的伏安特性'
xtitle2 = 'U (V)'
ytitle2 = 'I (mA)'
plt.plot(U2,I3,'x-',label='实验数据')
plt.title(title2)
plt.xlabel(xtitle2)
plt.ylabel(ytitle2)
plt.legend()
plt.grid(True)
plt.savefig('2.png',dpi=250)
plt.close()

plt.plot(U2,R3,'-',label='电阻值')
plt.title('非线性电阻(灯泡)的电阻值')
plt.xlabel(xtitle2)
plt.ylabel('R (Ω)')
plt.legend()
plt.grid(True)
plt.savefig('3.png',dpi=250)
plt.close()

# 3
title3 = '半导体二极管的伏安特性'
xtitle3 = 'U (V)'
ytitle3 = 'I (mA)'
plt.plot(U3,I4,'x-',label='实验数据')
plt.title(title3)
plt.xlabel(xtitle3)
plt.ylabel(ytitle3)
plt.legend()
plt.grid(True)
plt.savefig('4.png',dpi=250)
plt.close()
