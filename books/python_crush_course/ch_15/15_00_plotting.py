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

pyplot.savefig('squares_plot.png', bbox_inches='tight')
pyplot.show()

from random import choice

class RandomWalk():
    def __init__(self,num_points=50):
        self.num_points=num_points
        #all walks start at (0,0) :
        self.x_values=[0]
        self.y_values=[0]
        self.x_direction=0
        self.x_distance=0
        self.x_step=0
        self.y_direction=0
        self.y_distance=0
        self.y_step=0
        self.next_x=0
        self.next_y=0

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            self.x_direction=choice([1,-1])
            self.x_distance=choice([0,1,2,3,4])
            self.x_step=self.x_direction*self.x_distance

            self.y_direction=choice([1,-1])
            self.y_distance=choice([0,1,2,3,4])
            self.y_step=self.y_direction*self.y_distance

            #reject "move" that remain in place:
            if self.x_step==0 and self.y_step==0:
                print('STUB')
                print(self.x_step)
                print(self.x_direction)
                print(self.x_distance)
                print(self.y_step)
                print(self.y_direction)
                print(self.y_distance)

                continue


            self.next_x = self.x_values[-1] + self.x_step
            self.next_y = self.y_values[-1] + self.y_step

            self.x_values.append(self.next_x)
            self.y_values.append(self.next_y)

rw=RandomWalk()
rw.fill_walk()
pyplot.scatter(rw.x_values, rw.y_values, s=15)
pyplot.plot(rw.x_values, rw.y_values)
pyplot.show()
