# matplotlib.org
# pygal.org

print("##############################################################\n" + \
      "#                         chapter 15 matplot                 #\n" + \
      "##############################################################\n"   )

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

pyplot.title("(4) Scatter: Large Range!",   fontsize=24)
x_values=list(range(1,1000))
y_values=[x**2 for x in x_values]
pyplot.scatter(x_values, y_values, 
               edgecolor='none', c=y_values, cmap=pyplot.cm.Blues, s=1)
pyplot.axis([0, 1100, 0, (1000**2)+100])

pyplot.savefig('squares_plot.png', bbox_inches='tight')
pyplot.show()

from random import choice

class RandomWalk():
    def __init__(self,num_points=5000):
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
                continue


            self.next_x = self.x_values[-1] + self.x_step
            self.next_y = self.y_values[-1] + self.y_step

            self.x_values.append(self.next_x)
            self.y_values.append(self.next_y)



rw=RandomWalk()
rw.fill_walk()
point_numbers=list(range(rw.num_points))

#set pixels and resolutions:
pyplot.figure(dpi=128, figsize=(5,3) )
#plot all points:
pyplot.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=pyplot.cm.Blues, edgecolor='none',  s=1)
#plot starting point as a green dot:
pyplot.scatter(0, 0, c='green', edgecolors='none', s=100) 
#plot last point as a red dot:
pyplot.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100) 


#Remove the axes:
#pyplot.axes().get_xaxis().set_visible(False)
#pyplot.axes().get_yaxis().set_visible(False)

pyplot.show()



print("##############################################################\n" + \
      "#                         chapter 15 pygal                    #\n" + \
      "##############################################################\n"   )

from random import randint

class Die():
    """ A Class represeting a single die"""
    
    def __init__(self, num_sides=6):
        self.num_sides=num_sides

    def roll(self):
        """Return a random value between 1 and number of sides."""
        return randint(1, self.num_sides)

#create an object of type Die()
die=Die()
results=[]
# rolle the die and save the result in a list
for roll_number in range(100):
    result=die.roll()
    results.append(result)
print(results)
print

#Analyze the results:
occurance_frequencies=[]
for value in range(1, die.num_sides+1):
    occurance_frequency=results.count(value)
    occurance_frequencies.append(occurance_frequency)

print(occurance_frequencies)



import pygal

#hist=pygal.Bar()
hist=pygal.Histogram()
hist.title="Results of rolling one D6 1,000 times."
hist.x_labels=['1','2','3','4','5','6']
hist.x_title="Result"
hist.y_title="Frequency of Result"
hist.add('6 sided dice',occurance_frequencies)
#hist.render()
hist.render_to_file('die_visual.svg')




