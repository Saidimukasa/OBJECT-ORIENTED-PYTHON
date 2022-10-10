#A program to print firstt Hundred numbers
class Looping:
    def __init__(self,first,end):
        self.first=first
        self.end=end
        
    def __iter__(self):
    
      return self
    def __next__(self):
        if self.first<=self.end:
            x=self.first
            self.first+=1
            return x
        else:
            raise StopIteration
        
    def main():
        first=int(input("Enter the first number:"))
        end=int(input("Enter the end number:"))
        for i in Looping(first,end):
            print(i)
        