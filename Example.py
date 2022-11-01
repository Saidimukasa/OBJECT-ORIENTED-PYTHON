class Boy():
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def getName(self):
        return self.name

    def getOtherResult(self):
        print("My age is {}\n My gender is {} ".format(self.age,self.sex))

class Girl():
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def getName(self):
        return self.name

    def getOtherResult(self):
        print("My age is {}\n My gender is {} ".format(self.age,self.sex))

class Human():
    def __init__(self,Girl,Boy):
        self.girlname = Girl.getName()
        self.boyname = Boy.getName()
        self.otherGirl = Girl.getOtherResult()
        self.otherBoy = Boy.getOtherResult()
    def printGirlName(self):
        return self.girlname

    def printBoyName(self):
        return self.boyname

    def printOtherGirl(self):
        self.otherGirl

    def printOtherBoy(self):
        self.otherBoy

def main():
    girl = Girl("Joan","Female",23)
    boy = Boy("Peter", "Male", 30)

    human = Human(girl,boy)
    print(f"The boy name is {human.printBoyName()}")
    human.printOtherBoy
    print(f"The girl name is {human.printGirlName()}")
    human.printOtherGirl
main()
