class Uganda:
    def capitalCity(self):
        print("Kampala")
    def Nationallanguage(self):
        print("English")

class Tanzania:
    def capitalCity(self):
        print("Dodoma")
    def Nationallanguage(self):
        print("Swahili")

class India:
    def capitalCity(self):
        print("New Dehli")
    def Nationallanguage(self):
        print("Hindi")

def main():
    obj_uganda = Uganda()
    obj_tanzania = Tanzania()
    obj_india = India()

    for i in (obj_uganda, obj_tanzania, obj_india):
        i.capitalCity()
        i.Nationallanguage()

main()

