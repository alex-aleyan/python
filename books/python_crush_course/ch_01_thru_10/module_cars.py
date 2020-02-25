print("\n\n\n")
print("##############################################################\n" + \
      "#                         INCLUDING CLASSES MODULE           #\n" + \
      "##############################################################\n"   )

import module_reusable as funcs
import getpass
import json
import pickle

class BaseClass():

    def getAttributes(self):
        for attr, value in self.__dict__.iteritems():
            print attr, value



class UserClass(BaseClass):

    def __init__( self, 
                  first_name='', 
                  last_name='', 
                  age='', 
                  password=''):
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

    def __init__( self, 
                  make='none', 
                  model='none', 
                  year='none', 
                  gaslevel=0, 
                  vin='XXXXXXXXXXXXXXXXX', 
                  odometer=0 ):
        self.make=make.lower()
        self.model=model.lower()
        self.year=year
        self.vin=vin
        self.odometer=odometer
        self.gaslevel=gaslevel

    def setMake(self, make): # modify to check that a STRING is passed
        self.make=make
    def getMake(self):
        return self.make

    def setModel(self, model):# modify to check that a STRING is passed
        self.model=model
    def getModel(self):
        return self.model

    def setYear(self, year): # modify to check that an INTEGER is passed
        self.year=year
    def getYear(self):
        return self.year

    def setVin(self, vin): # modify to check that a STRING is passed
        self.vin=vin
    def getVin(self):
        return self.vin

    def setOdometer(self, odometer): # modify to check that a INTEGER is passed
        if odometer > self.odometer: self.odometer=odometer
    def getOdometer(self):
        return self.odometer

    def setGasLevel(self, gaslevel): # modify to check that a INTEGER is passed
        self.gaslevel=gaslevel
    def getGasLevel(self):
        return self.gaslevel



class CarBattery():
    def __init__( self, 
                  battery_size=70, 
                  charge_percent=20):

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



class ElectricCarClass(CarBattery, CarClass): #INHERITS CarClass!

    def __init__( self, 
                  make, 
                  model, 
                  year, 
                  vin, 
                  odometer, 
                  battery_size, 
                  charge_percent):

        ###EXAMPLE OF INHERITANCE:###
        CarClass.__init__( self, 
                           make=make,
                           model=model,
                           year=year,
                           vin=vin,
                           gaslevel='n/a',
                           odometer=odometer)

        CarBattery.__init__( self, 
                           battery_size=battery_size,
                           charge_percent=charge_percent)

    def setGasLevel(self, gaslevel): # modify to check that a INTEGER is passed
        print("This car is electric; try <self>.battery.setChargeLevel() ")
    def getGasLevel(self):
        print("This car is electric; try <self>.battery.getChargeLevel() ")


class CarGarage():
    def __init__(self, garageName):
        print("EMPTY INIT OF CarGarage() CLASS")
        self.filename=garageName+".txt"
        self.filenamepkl=garageName+".pkl"
        self.filenamejson=garageName+".json"
        self.car_list=[]

    def emptyGarage(self):
        del self.car_list[:]

    def addToGarage(self, car):
        self.car_list.append(car)

    def exportToPickleFile(self): #Save the new car to pickle file
        with open(self.filenamepkl, 'w') as pkl_file_obj:
            pickle.dump(self.car_list, pkl_file_obj)
    def importFromPickleFile(self): #Import saved data from pickle file
        with open(self.filenamepkl, 'r') as pkl_file_obj:
            self.car_list=pickle.load(pkl_file_obj)

    def showGarage(self):
        print("\nShowing garage content:")
        for car in self.car_list:
            print("\nNext car:")
            car.getAttributes()


