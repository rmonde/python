'''This is chapter 9 assignment'''

 

class Vehicle:

                def __init__(self):

                                self.make = 'make'

                                self.model = 'model'

                                self.year = 'dd-mm-yyyy'

                                self.Weight = 0

                                self.NeedsMaintenance = False

                                self.TripsSinceMaintenance = 0

                               

                #Setter methods

                def setMakeofVehicle(self,vMake):

                                self.make = vMake

               

                def setModelofVehicle(self,vModel):

                                self.model = vModel

                               

                def setYearofVehicle(self,vYear):

                                self.year = vYear

                               

                def setWeightofVehicle(self,vWeight):

                                self.Weight = vWeight

                               

                def repair(self):

                                self.NeedsMaintenance = False

                                self.TripsSinceMaintenance = 0

                               

                def __str__(self):

                                return 'The make of car is ' + self.make + '.The model of the car is ' + self.model + '.The weight of the car is ' + str(self.Weight) + 'KG.The year of manufacturing is ' + str(self.year) + '.'

                               

                               

class Car(Vehicle):

                def __init__(self,carName):

                                Vehicle.__init__(self)

                                self.name = carName

                                self.isDriving  = 'NaN'                     

                               

                def Drive(self):

                                self.isDriving  = True

                               

                def Stop(self):

                                self.isDriving = False

                                self.TripsSinceMaintenance +=1

                                if self.TripsSinceMaintenance > 100:

                                                self.NeedsMaintenance = True

                               

class Audi(Car):

                def __init__(self,carName):

                                Car.__init__(self,carName)

 

class Merc(Car):

                def __init__(self,carName):

                                Car.__init__(self,carName)

                               

class Jaguar(Car):

                def __init__(self,carName):

                                Car.__init__(self,carName)

 

myAudi = Audi('Audi')

benz = Merc('Mercedeez')

jag = Jaguar('Jagaur')

 

print('My car name is:',myAudi.name)

myAudi.setMakeofVehicle('Metal')

myAudi.setModelofVehicle('Q7')

myAudi.setWeightofVehicle(300)

myAudi.setYearofVehicle(2017)

myAudi.Drive()

myAudi.Stop()

myAudi.Stop()

myAudi.Stop()

for i in range(0,99):

                myAudi.Stop()

print(myAudi)

print(myAudi.TripsSinceMaintenance)

print(myAudi.NeedsMaintenance)

print('------------------------')

print('My car name is:',benz.name)

benz.setMakeofVehicle('Brass')

benz.setModelofVehicle('S-Class')

benz.setWeightofVehicle(400)

benz.setYearofVehicle(2015)

benz.Drive()

benz.Stop()

benz.Stop()

benz.Stop()

for i in range(0,98):

                benz.Stop()

print(benz)

print(benz.TripsSinceMaintenance)

print(benz.NeedsMaintenance)

print('------------------------')

print('My car name is:',jag.name)

jag.setMakeofVehicle('Metal')

jag.setModelofVehicle('abc')

jag.setWeightofVehicle(3000)

jag.setYearofVehicle(2015)

jag.Drive()

jag.Stop()

jag.Stop()

jag.Stop()

for i in range(0,200):

                jag.Stop()

print(jag)

print(jag.TripsSinceMaintenance)

print(jag.NeedsMaintenance)

jag.repair()

print(jag.TripsSinceMaintenance)

print(jag.NeedsMaintenance)

 