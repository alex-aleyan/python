import matplotlib.pyplot as pyplot

x_values=[1,2,3,4,5]
y_values=[x**2 for x in x_values]

pyplot.title("(1) Plot: Square Numbers",   fontsize=24)
pyplot.xlabel("Value",           fontsize=14)
pyplot.ylabel("Square of Value", fontsize=14)
pyplot.tick_params(axis='both', labelsize=8)
pyplot.plot(x_values, y_values, linewidth=1)

pyplot.show()

pyplot.title("(2) Scatter: Square Numbers",   fontsize=24)
pyplot.xlabel("Value",           fontsize=14)
pyplot.ylabel("Square of Value", fontsize=14)
pyplot.tick_params(axis='both', labelsize=8)
pyplot.scatter(x_values, y_values) #,s=200

pyplot.show()

pyplot.title("(3) Plot+Scatter: Squared Numbers",   fontsize=24)
pyplot.xlabel("Value",           fontsize=14)
pyplot.ylabel("Square of Value", fontsize=14)
pyplot.tick_params(axis='both', which='major', labelsize=8)
pyplot.plot(x_values, y_values, linewidth=1)
pyplot.scatter(x_values, y_values, edgecolor='none', c='red', s=1)
pyplot.axis([0, 6, 0, 30])

pyplot.show()

pyplot.title("(4) Plot+Scatter: Large Range!",   fontsize=24)
x_values=list(range(1,1000))
y_values=[x**2 for x in x_values]
pyplot.scatter(x_values, y_values, 
               edgecolor='none', c=y_values, cmap=pyplot.cm.Blues, s=1)
pyplot.axis([0, 1100, 0, (1000**2)+100])

pyplot.show()
