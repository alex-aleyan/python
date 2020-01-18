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

