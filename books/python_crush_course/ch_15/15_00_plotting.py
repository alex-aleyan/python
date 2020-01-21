import matplotlib.pyplot as pyplot

squares=[1,4,9,16,25]

pyplot.plot(squares, linewidth=1)

pyplot.title("Square Numbers",   fontsize=24)
pyplot.xlabel("Value",           fontsize=14)
pyplot.ylabel("Square of Value", fontsize=14)

pyplot.tick_params(axis='both', labelsize=8)

pyplot.show()
