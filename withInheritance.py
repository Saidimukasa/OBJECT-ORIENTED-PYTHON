class Birds:
    def __init__(self,day):
        self.day = day
    def intro(self):
        print("Birds can fly but some cant")
    
    def flight(self):
        print("some birds can fly")

    def gestation(self):
        print(f"My gestation peroid is {self.day}")

class  Hen(Birds):
    def __init__(self,day):
        super().__init__(day)
        self.name = "Hen"
        self.day = day
    def flight(self):
        print (f"{self.name} cannot fly")
        
class Parrot(Birds):
    def __init__(self,day):
        super().__init__(day)
        self.name = "Parrot"
        self.day = day
    def flight(self):
        print(f"{self.name} can fy")

def main():
    hen = Hen(21)
    parrot = Parrot(31)

    hen.intro()
    hen.flight()
    hen.gestation()
    parrot.intro()
    parrot.flight()
    parrot.gestation()
main()