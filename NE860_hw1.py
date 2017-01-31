from __future__ import division
import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, np.pi, 100)

y=[]
x2=[]
for i in x:
    ans = (1/(4*np.pi))*(2+2*np.cos(i))**(3/2)/(np.cos(i)+1)
    y.append(ans)
    ans2 = np.cos(i)
    x2.append(ans2)

y0=[]
y1=[]
y2=[]
y3=[]
ans0=0
ans1=0
ans2=0
ans3=0
for i in np.linspace(3.14,0,100):
    ans0 = (1/2)*(1/(4*np.pi))*(1+2*np.cos(i)+1)**(3/2)*(np.pi/100)/(np.cos(i)+1) + ans0
    ans1 = (3/2)*(1/(4*np.pi))*(1+2*np.cos(i)+1)**(3/2)*np.cos(i)*(np.pi/100)/(np.cos(i)+1) + ans1
    ans2 = (5/2)*(1/(4*np.pi))*(1+2*np.cos(i)+1)**(3/2)*(1/2)*(3*np.cos(i)**2 - 1)*(np.pi/100)/(np.cos(i)+1) + ans2
    ans3 = (7/2)*(1/(4*np.pi))*(1+2*np.cos(i)+1)**(3/2)*(1/2)*(5*np.cos(i)**3 - 3*np.cos(i))*(np.pi/100)/(np.cos(i)+1) + ans3
    
#    y0.append(ans0)
#    y1.append(ans1)
#    y2.append(ans2)
#    y3.append(ans3)
    

for i in np.linspace(0,np.pi,100):
    y0.append(ans0 * 1)
    y1.append(ans1 * np.cos(i))
    y2.append(ans1 * np.cos(i) + (1/2)*ans2*(3*np.cos(i)**2-1))
    y3.append(ans1 * np.cos(i) + (1/2)*ans2*(3*np.cos(i)**2-1) + (1/2)*ans3*(5*np.cos(i)**3-3*np.cos(i)))

x3=[]
xl = np.linspace(0, np.pi, 100)
for i in xl:
    x3.append(np.cos(i))

plt.figure
params = {'mathtext.default': 'regular' }          
plt.figure(figsize = (15,10.5))
plt.rcParams.update(params)

plt.xlabel(r'$cos(\theta)$',  fontname="Arial", fontsize=30)
plt.tick_params(which='major', length=15, labelsize=25)
plt.tick_params(which='minor', length=7)
plt.grid(True, which='minor', color='lightgrey', linestyle='-')
plt.grid(True, which='major', color='dimgrey', linestyle='-')

plt.ylabel(r'$P(\mu)$', fontname="Arial", fontsize=30)
plt.title('Probability of Scatter', fontname="Arial", fontsize=30)
# plt.title ("Soft Tissue Results",fontsize=18)
plt.rc('font',family='Arial')

p0 = plt.plot(x3, y0, 'y-', label='zeroth', linewidth = 4)
p1 = plt.plot(x3, y1, 'r-', label='First', linewidth = 4)
p2 = plt.plot(x3, y2, 'b-', label='Second', linewidth = 4)
p3 = plt.plot(x3, y3, 'g-', label='Third', linewidth = 4)
p4 = plt.plot(x2, y, 'k-', label='Function',  linewidth = 4)

plt.legend(loc=2,prop={'size':17})

plt.show
