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

regression_line=[ (m*x)+b for x in xs]
#regression_line=[]
#for x in xs:
#    regression_line.append((m*x)+b)

set_x=7
get_y=(m*set_x)+b
print(get_y)

import matplotlib.pyplot as pyplot
from matplotlib import style
style.use('ggplot')
pyplot.scatter(xs,ys,color='blue')
pyplot.scatter(set_x,get_y,color='green')
pyplot.plot(xs,regression_line)
"""
for point in zip(xs,regression_line):
    #label="{:.2f}".format(xs)
    pyplot.annotate('local max',
                    #label,
                    (xs,regression_line),
                    textcoords="offset points",
                    xytext=(0,10),
                    ha='center'
                    )
"""
pyplot.show()

