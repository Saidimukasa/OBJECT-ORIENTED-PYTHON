# Private Data Hiding 
# This is similar to the Protected Data Hiding but the difference is that the Private Data Hiding is only accessible within the class and not outside the class.

class Base:
    def __init__(self, name, age):
        self.name = name
        self.__age = age #This means the Age Variable will be private and only accessible within the class and not outside the class.
        
class derived(Base):
    def __init__(self, name, age, address):
        Base.__init__(self, name, age)
        self.address = address
        # Modifying the private member
        self.__age=24
        
objects = derived("Mukasasaidi", 23, "Dar es Salaam")
print(objects.age) #This wil print an error because the age variable is private and not accessible outside the class

        