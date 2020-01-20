print("\n\n\n")
print("##############################################################\n" + \
      "#                         INCLUDING FUNCS MODULE             #\n" + \
      "##############################################################\n"   )

import module_funcs as funcs
import getpass

class user_class():

    def __init__(self, first_name='', last_name='', age='', password=''):
        while True: 
            if first_name == '':
                user_prompt="Provide your first name: "
                self.first_name=funcs.get_alpha(user_prompt).lower()
            else:
                self.first_name=first_name
         
            
            if last_name == '':
                user_prompt="Provide your last name: "
                self.last_name=funcs.get_alpha(user_prompt).lower()
            else:
                self.last_name=last_name
            
            if age == '':
                user_prompt="Please provide your age: "
                self.age=funcs.get_numeric(user_prompt)
            else:
                self.age=age
            
            if password == '':
                user_prompt="Please provide a password: "
                #new_user['password']=get_alphanumeric(user_prompt)
                self.password=getpass.getpass(user_prompt)
            else:
                self.password=password
            
            print("\nThis is the data provided by the user:")
            self.getAttributes();

            user_prompt="Accept the provided data(yes/no)?"

            user_answer=raw_input(user_prompt)
            if user_answer.lower() == 'yes' or user_answer.lower == 'y': 
                print("Saving the new user")
                break    
            if user_answer.lower() == 'no' or user_answer.lower() == 'n': #dismiss info
                print("Dismissing the provied info")
    
    def getAttributes(self):
        for attr, value in self.__dict__.iteritems():
            print attr, value


