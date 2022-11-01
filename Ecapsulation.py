# Ecapsulation refers to the Technique of hiding the data members and member functions of a class from the outside world.
# These Data members can oly be accesed once been approaved 
# The Object oriented Ecapsulation is also known as Data Hiding and uses the Concept of Protected and Private Access Specifiers.


# Protected Access Specifiers or Data Hiding
class Base:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # Creating  a protected member we use the Underscore
        self._name=name #This means the Name Variable will be protected
        

class Derived(Base):
    def __init__(self, name, age, address):
        Base.__init__(self, name, age)
        self.address = address
        # Creating a private member we use the Double Underscore
        self.__name=name #This means the Name Variable will be private
        
        # Modifying the protected member
        self._name="Mukasasaidi23"
        
objects = Derived("Mukasasaidi", 23, "Dar es Salaam")

# Accesiing the protected member
print(objects._name)