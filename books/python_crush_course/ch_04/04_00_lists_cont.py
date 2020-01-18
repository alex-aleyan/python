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



# chapter 3

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
      "#                         chapter 3                          #\n" + \
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
