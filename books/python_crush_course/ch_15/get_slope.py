from statistics import mean
import numpy as np

#xs=np.array([1,2,3,4,5], dtype=np.float64) 
#ys=np.array([5,4,6,5,6], dtype=np.float64) 

xs=np.array([500,750,1000,1500,1750,2000,2500,3000], dtype=np.float64) 
ys=np.array([2,2.4,2.7,3.2,4,4.6,6.4,7.8], dtype=np.float64) 

def best_fit_slope(xs,ys):
    m=((( mean(xs)*mean(ys)) - mean(xs*ys) ) / (( mean(xs)*mean(xs)) - mean(xs*xs)))
    b=mean(ys) - m*mean(xs)
    return m,b

m,b=best_fit_slope(xs,ys)
print(m,b)

set_x=7
get_y=(m*set_x)+b

regression_line=[ (m*x)+b for x in xs]
regression_line=[]
for x in xs:
    regression_line.append((m*x)+b)


import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
plt.scatter(xs,ys,color='#003F72')
plt.plot(xs,regression_line)



plt.show()

