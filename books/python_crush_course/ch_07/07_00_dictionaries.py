#Simplly prints the message:
hello_message_str="Hello Python World!"
print(hello_message_str)

hello_message_str="Reusing the var to hold a new message!"
print(hello_message_str)



name="ada lovelace"
#Capitalize 1st letter of every word: "ada lovelace" -> "Ada Lovelace"
name=name.title()
print(name)
#Capitalize all letter of every word: "Ada Lovelace" -> "ADA LOVELACE"
name=name.upper()
print(name)
#all letter are non capilzied: "ADA LOVELACE" -> "ada lovelace"
name=name.lower()
print(name)



first_name="sasha"
last_name="aleyan"
full_name=first_name + " " + last_name
print(full_name.title())



#using quotes in the string:
msg_with_quotes1='Mixing "quotes"'
print(msg_with_quotes1)
msg_with_quotes2="Mixing 'quotes'"
print(msg_with_quotes2)
hello_message="\tHello, " + full_name.title() + "!!!\n" \
              + "\tHow's it going?"
print(hello_message)



name_strip="     somename      "
print(name_strip)
name_strip=name_strip.rstrip()
print(name_strip)
name_strip=name_strip.lstrip()
print(name_strip)



#escaping the apostrophy:
message='Python\'s awesome syntax utilizes the same escape tricks as bash/C'
print(message)



#math:
print(2**2 + 3*4)
print(2*1.5)



#converting int to string before printing:
age=15
# concatenate into: "Happy 15th birthday"
print("Happy " + str(age) + "th birthday")



print("\n\n\n")
print("##############################################################\n" + \
      "#                         chapter 3                          #\n" + \
      "##############################################################\n"   )



bicycles = [ 'trek', \
             'cannondale', \
             'redline', \
             'specialized' ]

print(bicycles)
print(bicycles[0] + '; ' + bicycles[1] )

# Capitalize 1st letter of each name:
print("\nFirst item: " + bicycles[0].title()  + '\n' + \
         "Last item: " + bicycles[-1].title() + "\n"     )

print("Inverting:" + bicycles[-1].title() + '; ' + bicycles[-2].title() )



driver = [ 'mike', \
           'matt', \
           'john'  ]

make = [ 'toyota', \
         'nissan', \
         'honda'   ]

model = [ 'ae86' , \
          '180sx', \
          's2000'  ]

print('\n')
print(driver[0].title() + "--" + make[0].title() + "--" + model[0].upper() )
print(driver[1].title() + "--" + make[1].title() + "--" + model[1].upper() )
print(driver[2].title() + "--" + make[2].title() + "--" + model[2].upper() )

print('\n')
model[0]='mr2'
print(driver[0].title() + "--" + make[0].title() + "--" + model[0].upper() )
print(driver[1].title() + "--" + make[1].title() + "--" + model[1].upper() )
print(driver[2].title() + "--" + make[2].title() + "--" + model[2].upper() )

print('\nAppending Andy to last column')
driver.append('andy') 
make.append('mazda')
model.append('miata')
print(driver)
print(make)
print(model)

# "del <list[<NUM>]>" - deleting a specific entry from the list:
print('\nDeleting column[2]')
del driver[2]
del make[2]
del model[2]
print(driver)
print(make)
print(model)

# ".pop()" - method to delete a list's tail entry:
print("\nUsing .pop() to remove at the tail:")
driver.pop()
make.pop()
model.pop()
print(driver)
print(make)
print(model)

# ".pop(0)" - delete a list's head entry:
print("\nUsing .pop(0) to remove at the head:")
first_driver_gone = driver.pop(0)
first_make_gone   = make.pop(0)
first_model_gone  = model.pop(0)

print("First driver, "        + first_driver_gone.title() +  \
      ", drove away driving " + first_make_gone.upper()   +  \
      " "                     + first_model_gone.upper()     )

# .remove() - removing by value an entry from a list.
print("\nUsing .remove() to remove by value:")
print(driver); print(make); print(model)
driver.remove('matt')
make.remove('nissan')
model.remove('180sx')
print(driver); print(make); print(model)


# .sort() - sorting a list permanenty:
print("\nUsing <LIST>.sort()")
make = [ 'toyota', \
         'nissan', \
         'honda' , \
         'mazda'   ]
print(make)


make.sort()
print(make)

make.sort(reverse=True)
print(make)


# sorted(<LIST>) - sorting a list without altering the original list:
print("\nUsing sorted(<LIST>)")
make = [ 'toyota', \
         'nissan', \
         'honda' , \
         'mazda'   ]
print(make)
sorted_make=sorted(make)
print(sorted_make)


# <LIST>.reverse() - reversing the order of entries in the list permanenty:
print("\nUsing <LIST>.reverse()")
make = [ 'toyota', \
         'nissan', \
         'honda' , \
         'mazda'   ]

make.reverse()
print(make)


# len(<LIST>) - determining number of entries in the list:
print("\nUsing len(<LIST>):")
make = [ 'toyota', \
         'nissan', \
         'honda' , \
         'mazda'   ]

entry_number=len(make)
print(str(entry_number))


print("\n\n\n")
print("##############################################################\n" + \
      "#                         chapter 4                          #\n" + \
      "##############################################################\n"   )



list_of_magicians=[ 'alice', \
                    'david', \
                    'job'   ]

# for <i> in <list> - just like bash!
print("\nLooping: for <i> in <list>")
for a_magician in list_of_magicians:
    print("\t" + a_magician.title() + ", nice illusion!")
    print("\t" "Show us more tricks, Mr/Ms " + a_magician.title() )
    print("\n") # better to separate \n this way we don't have to move \
                # it around from within a string when inserting more prints

print("Thank you all for the show!")


# for <i> in range(<start with value>,<terminate before value>)
print("\nLooping: for <i> in range(<value>,<value>")
for a_number in range(0,3) :
    print("Number: " + str(a_number))
    print("A Magician: " + str(list_of_magicians[a_number]) )

# list(range(<start_value,<end_value>)) - create list of numbers
print("\nUsing range(0,10):")
list_of_numbers=list(range(0,10))
print(list_of_numbers)


# list(range(<start_value,<end_value>,<increment value>)) - create list of numbers:
print("\nUsing range(0,20,2):")
list_of_even_numbers=list(range(0,20,2))
print(list_of_even_numbers)

# Using range with math to create any set of numbers you desire:
print("\nUsing range(1,11) with math funcs to create series of sqrd nums:")
list_of_squared_values=[]
for value in range(1,11):
    list_of_squared_values.append(value**2)

print(list_of_squared_values)

# List COMPREHENSIONS:
print("\nUsing list comprehensions: list=[<func1>(var) for var in <func2>() ]")
squares=[value**2 for value in range(1,11)]
print(squares)



# Simple statistics:
print("\nUsing simple statistics: min, max, sum")
digits=[]
digits=range(1,10) # create a list of 1,2,..,9
digits.append(0)  # append 0: 1,2,..,9,0
print(digits)
print(min(digits))
print(max(digits))
print(sum(digits))



# Slicing lists:
print("\nSlicing lists:")

players=['charles00',  \
         'martin01',   \
         'michael02',  \
         'florence03', \
         'eli04'       ]

print("All:")
print(players)

print("[0,3]:")
print(players[0:3])

print("[1,4]:")
print(players[1:4])

print("[ ,4]:")
print(players[:4])

print("[2, ]:")
print(players[2:])

print("[-3,]:")
print(players[-3:])

print("\nLooping thru players[:3]")
for player in players[:3]: 
    print(player.title())
print("\nLooping thru players[-3:]")
for player in players[-3:]: 
    print(player.title())

#Copying a list:
print("\nCopying players list: new_list = players[:]")
new_list=players[:]
print('new_list= ' + str(new_list) )

# Aliasing a list:
print("\nAliasing a list:")
players_alias=players
print('players_alias= ' + str(players_alias) )
players.append("robert")
print('players_alias= ' + str(players_alias) )



# TUPLE - constant, immodifiable list:
print("\nTUPLES:")

dimensions_tuple=(200,\
                  50  )
print(dimensions_tuple[0])
print(dimensions_tuple[1])

print("\nLooping thru TUPLE")
for dimension in dimensions_tuple:
    print(dimension)

print("\nRedefining entire TUPLE:")
dimensions_tuple=(400,\
                  800 )
for dimension in dimensions_tuple:
    print(dimension)



print("\n\n\n")
print("##############################################################\n" + \
      "#                         chapter 5                          #\n" + \
      "##############################################################\n"   )


cars=['honda',  \
      'toyota', \
      'bmw',    \
      'subaru'  ]

print("")
print("Using 'if-else' to determine if .upper() or .title() to be used:")
print("noticed how we use .lower() in \"if car.lower() == 'bmw' \"")
for car in cars:
    if car.lower() == 'bmw':
        print( car.upper() )
    else:
        print( car.title() )

print("")
print("Same a above but using \"if car.lower() != 'bmw' \":")
for car in cars:
    if car.lower() != 'bmw':
        print( car.title() )
    else:
        print( car.upper() )

print("\nCheck if string TOYOTA is in the list!")
print("Notice how we use the .lower() function")
if 'TOYOTA'.lower() in cars:
    print("TOYOTA is in cars list")


print("\nTesting items of one list against items in another list:")
japanese_cars=['toyota','honda','nissan','subaru','mitsubishi']
for a_car in cars :
    if a_car in japanese_cars :
        print("The car is a japanese car!")
    else:
        print("The " + a_car + " is NOT a japanese car!")


print("")
print("Performing numerical comparisons to check if numbers are within 0 thru 25 range")
#numbers=[15, 25, 35, 5, 13]
list_of_numbers=list( range(-3,29,1) )
for a_number in list_of_numbers:
    if a_number < 0 or a_number > 25:
        print( str(a_number) + " is OOR" )
    elif a_number >= 0 and a_number <= 10:
        print( str(a_number) + " is positive [0;10]" )
    elif a_number > 10 and a_number <= 20:
        print( str(a_number) + " is within (10;20]" )
    elif a_number > 20:
        print( str(a_number) + " is within (20;25]" )
    else:
        print("ERROR: this condition should never be hit!")


print("\nChecking if list is empty:")
empty_list=[]
if empty_list :
    print("list is not empty")
else :
    print("list is empty")



print("\n\n\n")
print("##############################################################\n" + \
      "#                         chapter 6 DICTIONARIES             #\n" + \
      "##############################################################\n"   )

car={'year'   : 1995,   \
     'make'   : 'toyota', \
     'model'  : 'soarer'  }

print(str(car['year']) + " " + car['make'] + " " + car['model'])


car['color']='black'
car['country']='japan'

print('car: ' + str(car))

print("")
new_car={}
print('new_car (empty dictionary): ' + str(new_car))
new_car['year']=1995
new_car['make']='nissan'
new_car['model']='180sx'
new_car['color']='white'
new_car['country']='japan'
print('new_car: ' + str(new_car))

if new_car['color'] == 'white' :
    new_car['color']='black'
    new_car['colour']='black'
    new_car['trim']='se'

print('new_car: ' + str(new_car))

del new_car['trim']

print('new_car (after deleting \"trim\"): ' + str(new_car))

print("\nLooping thru dictionary's key/value pairs:")
for key, value in new_car.items() :
    print(str(key) + " " + str(value))

print("\nLooping thru dictionary's keys:")
for key in new_car.keys() :
    print(str(key))
print("Sorted keys:")
for key in sorted(new_car.keys()) :
    print(str(key))

print("\nLooping thru dictionary's values:")
for value in new_car.values() :
    print(str(value))
print("Sorted values:")
for value in sorted(new_car.values()) :
    print(str(value))
print("Ignore duplicates:")
for value in set(new_car.values()) :
    print(str(value))


print("\n\nDictionary in a dictionary:")

drivers= {
    'aleyana': {'first' : 'alex',
                'last'  : 'aleyan',
                'car'   : '180sx'},
    'desantism': {'first' : 'mallory',
                  'last'  : 'desantis',
                  'car'   : 'saab'},
    'aleyano' : {'first' : 'olivia',
                 'last'  : 'aleyan',
                 'car'   : 'gtr'}
    }

for driver, driver_info in drivers.items():
    print("")
    print("driver alias: " + driver                            )
    print("first name: "   + str(driver_info['first']).title() )
    print("last name: "    + str(driver_info['last']).title()  )
    print("car name: "     + str(driver_info['car']).upper()   )

