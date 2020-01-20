print("\n\n\n")
print("##############################################################\n" + \
      "#                         INCLUDING FUNCS MODULE             #\n" + \
      "##############################################################\n"   )

import module_funcs as funcs
import getpass

class BaseClass():
    def getAttributes(self):
        for attr, value in self.__dict__.iteritems():
            print attr, value

class UserClass(BaseClass):

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


class CarClass(BaseClass):

    def __init__(self, make, model, year, gaslevel=0, vin='XXXXXXXXXXXXXXXXX', odometer=0):
        self.make=make.lower()
        self.model=model.lower()
        self.year=year
        self.vin=vin
        self.odometer=odometer
        self.gaslevel=gaslevel

    def setMake(self, make): # modify to check that a STRING is passed
        self.make=make
    def setModel(self, model):# modify to check that a STRING is passed
        self.model=model
    def setYear(self, year): # modify to check that an INTEGER is passed
        self.year=year
    def setVin(self, vin): # modify to check that a STRING is passed
        self.vin=vin
    def setOdometer(self, odometer): # modify to check that a INTEGER is passed
        if odometer > self.odometer: self.odometer=odometer
    def setGasLevel(self, gaslevel): # modify to check that a INTEGER is passed
        self.gaslevel=gaslevel

    def getMake(self):
        return self.make
    def getModel(self):
        return self.model
    def getYear(self):
        return self.year
    def getVin(self):
        return self.vin
    def getOdometer(self):
        return self.odometer
    def getGasLevel(self):
        return self.gaslevel

class car_battery():
    def __init__(self, battery_size=70, charge_percent=20):
        self.battery_size=battery_size
        self.charge_percent=charge_percent
    def setChargeLevel(self, charge_percent): # modify to check that a INTEGER is passed
        self.charge_percent=charge_percent
    def getChargeLevel(self):
        return self.charge_percent
    def setBatterySize(self, battery_size): # modify to check that a INTEGER is passed
        self.battery_size=battery_size
    def getBatterySize(self):
        return self.battery_size

class ElectricCarClass(CarClass):

    def __init__(self, make, model, year, vin, odometer, battery_size, charge_percent):

        # INHERITANCE:
        #super(ElectricCarClass, self).__init__(make,model,year,vin,odometer)
        CarClass.__init__(self, make,model,year,vin,odometer)

        # AGGREGATION:
        self.battery=car_battery()

    def setGasLevel(self, gaslevel): # modify to check that a INTEGER is passed
        print("This car is electric; try <self>.battery.setChargeLevel() ")
    def getGasLevel(self):
        print("This car is electric; try <self>.battery.getChargeLevel() ")





