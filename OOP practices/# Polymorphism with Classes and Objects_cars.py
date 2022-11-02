# Polymorphism with Classes and Objects

class Car:
    def __init__(self, name):
        self.name = name
        # self.color = color
    def intr(self):
        print("These are Car details")
  
    #Toyota   
class Toyota(Car):
    def __init__(self,name,color,price):
        Car.__init__(self,name)
        self.price=price
        self.color=color
        self.name="Toyota"
    def intr(self):
        print(f"These are {self.name} details")
    def speed(self):
        print("Toyota is fast")
    def __str__(self):
      return f"Name: {self.name} Color: {self.color} Price: {self.price}"
   
    #Honda class  
class Honda(Car):
        def __init__(self,name,color,price):
            Car.__init__(self,name)
            self.price=price
            self.color=color
            self.name="Honda"
        def intr(self):
            print(f"These are {self.name} details")
        def speed(self):
            print("Toyota is fast")
        def __str__(self):
         return f"Name: {self.name} Color: {self.color} Price: {self.price}"
   

    #Bugatti class     
class Buggati(Car):
    def __init__(self,name,color,price):
        Car.__init__(self,name)
        self.price=price
        self.color=color
        self.name="Buggati"
        # Introduction
    def intr(self):
        print(f"These are {self.name} details")
    # speed details   
    def speed(self):
        print("Buggati is very fast")
    # Full information   
    def __str__(self):
        return f"Name: {self.name} Color: {self.color} Price: {self.price}"
        
    #The Main Function    
def main():
    # The car instances
    toyota=Toyota("Toyota","Red",2000000)
    honda=Honda("Honda","Red",5000000)
    bugatti=Buggati("Buggati","Black",6000000)
    print(toyota)
    print(honda)
    print(bugatti)
    
        #loop will help to print all the details of the cars 
    for car in (toyota,honda,bugatti):
        car.intr()
        car.speed()
    
main()
        
        
    
    