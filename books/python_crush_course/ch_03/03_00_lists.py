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



# Chapter 3

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


print('\nDeleting column[2]')
del driver[2]
del make[2]
del model[2]
print(driver)
print(make)
print(model)

print('\nPopping:')
driver.pop()
make.pop()
model.pop()
print(driver)
print(make)
print(model)

first_driver_gone = driver.pop(0)
first_make_gone   = make.pop(0)
first_model_gone  = model.pop(0)

print("First driver "       + first_driver_gone.title() + " " + \
      "drove away driving " + first_make_gone.upper()   + " "   \
                            + first_model_gone.upper() )
