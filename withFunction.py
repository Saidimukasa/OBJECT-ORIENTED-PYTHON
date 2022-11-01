class Tomato:
    def types(self):
        return "I ama vegetable"

    def color(self):
        return "red"

class Apple:
    def types(self):
        return "I m a fruit"
    def color(self):
        return "green"

def fun(obj):
    print(obj.types())
    print(obj.color())

def main():
    obj_tomato = Tomato()
    obj_apple = Apple()
    fun(obj_tomato)
    fun(obj_apple)
main()