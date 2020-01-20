print("\n\n\n")
print("##############################################################\n" + \
      "#                         INCLUDING FUNCS MODULE             #\n" + \
      "##############################################################\n"   )

new_user={}

def get_alpha(user_prompt='gets abc..xyzABC..XYZ'):
    while True: #make sure the answer has no numbers in the name
        user_answer=raw_input(user_prompt)
        if user_answer.isalpha(): break    
    return user_answer

def get_numeric(user_prompt='gets 0-9'):
    #Loops if age has non-integer value until age is provided as an integer
    while True:
        try:
            user_answer=int(raw_input(user_prompt))
        except ValueError:
            print("Sorry, it has gotten to be an integer")
        else: break
    return user_answer

def get_alphanumeric(user_prompt='gets 0..9abc...xyzABC...XYZ'):
    while True: # Loop until password with no white space is provide:
        user_answer=raw_input(user_prompt)
        if (' ' in user_answer) != True: break
    return user_answer

def get_username(first_name, last_name):
    return str( first_name[0] + last_name )


def get_newuser():
    user_prompt="Provide your first name: "
    new_user['first_name']=get_alpha(user_prompt).lower()
    print(new_user['first_name'])
    
    user_prompt="Provide your last name: "
    new_user['last_name']=get_alpha(user_prompt).lower()
    print(new_user['last_name'])
    
    user_prompt="Please provide your age: "
    new_user['age']=get_numeric(user_prompt)
    print(new_user['age'])
    
    import getpass
    user_prompt="Please provide a password: "
    #new_user['password']=get_alphanumeric(user_prompt)
    new_user['password']=getpass.getpass(user_prompt)
    print(new_user['password'])
    
    #ACCEPT THE PROVIDED DATA:
    print("\nShow provided data:")
    for key, data in new_user.items(): # show entered data
        if key != 'password': print( str(key.replace("_"," ")) + ": " + str(data) )
        #print( str(key.replace("_"," ")) + ": " + str(data) )
    
    user_prompt="Accept the provided data(yes/no)?"
    while True: 
        user_answer=raw_input(user_prompt)
        if user_answer.lower() == 'yes' or user_answer.lower == 'y': 
            print("Saving the new user")
            return new_user
            break    
        if user_answer.lower() == 'no' or user_answer.lower() == 'n': #dismiss info
            print("Dismissing the provied info")
            break    


def make_pizza(size, 
               *toppings):
    print("Pizza size: " + str(size) + "\"")
    print("Print the toppings:")
    for topping in toppings:
        print( "- " + str(topping) )



