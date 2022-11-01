from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
    @abstractmethod
    def gestation(self):
        pass

class Cow(Animal):
    def sound(self):
        print("Moew")
    def gestation(self):
        print("8 months")
class Dog(Animal):
    def sound(self):
        print("bark")
    def gestation(self):
        print("5 months")
    
class Snake(Animal):
    def sound(self):
        print("Hiss")
    def gestation(self):
        print("3 months")

def main():
    
    obj_cow=Cow()
    obj_dog=Dog()
    obj_snake=Snake()
    for i in (obj_cow,obj_dog,obj_snake):
        i.gestation()
        i.sound()

main()


