# Polymorphism is the ability to take on many forms
# The term "polymorphism" is derived from two Greek words: poly (many) and morphs (forms).
# These are functions that can be used in different ways.

# Example 1
# The Len() function can be used on a string and a list
# print(len("Mukasasaidi"))
# print(len(["Mukasasaidi", "Mukasasaidi23"]))

# # Sample of User Defined Polymorhic Functions
# def add(x, y, z=0):
#     return x + y + z

# print(add(2, 3))
# print(add(2, 3, 4))

# Polymorhism with Class methods 

from tkinter import N


class Uganda:
    def capital(self):
        print("Kampala is the capital of Uganda")
    
    def language(self):
        print("English is the primary language of Uganda")
    
    def type(self):
        print("Uganda is a developing country")
        
class Kenya:
    def capital(self):
        print("Nairobi is the capital of Kenya")
    
    def language(self):
        print("Swahili is the primary language of Kenya")
    
    def type(self):
        print("Kenya is a developing country")
        
        
        
def main():
    country1 = Uganda()
    country2=Kenya()
    
    for country in country1, country2:
        country.capital()
        country.language()
        country.type()
        
if __name__ == "__main__":
    main()
    
# # Polymorphism with Inheritance

class Bird:
    def __init__(self,name):
        self.name = name
    def flight(self):
        print(f"{self.name} can fly")
    
class Sparrow(Bird):
    def __init__(self,name):
        super().__init__(name)
        self.name = name    
    def flight(self):
        print(f"{self.name} can fly but not very far") 
class Ostrich(Bird):
    def __init__(self,name):
        super().__init__(name)
        self.name = name
        # This is using the polymorphism method of inheritance to override the flight method of the Bird class since it the Ostrich cannot be able to fly
    def flight(self):
        print(f"{self.name} cannot fly")
    
def main():
    sparrow=Sparrow("Sparrow")
    sparrow.flight()
    ostritch=Ostrich("Ostrich")
    ostritch.flight()
if __name__ == "__main__":
    main()
    
    
# # Polymorphism with a Function and Objects
class Animals:
    def __init__(self, name):
        self.name = name
    def sound(self):
        return self.name + " makes a sound"
  
# Creating a class Dog and this an Independent class  
class Dog():
    def __init__(self,name):
        self.name = name
    # Function Sound for Dog  
    def sound(self):
        return self.name + " barks"
# passing and object to a function
def func(obj):
    obj.sound()
    
    
def main():
    dog = Dog("Dog")
    print(dog.sound())
    
    cat = Animals("Cat")
    print(cat.sound())
main()    