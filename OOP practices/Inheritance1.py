from __future__ import print_function

# Inheritence is a way of creating a new class for using details of an existing class without modifying it.

# Parent class
class Student:
    def __init__(self,First_name,Last_name,age,Regno,course):
        self.First_name=First_name
        self.Last_name=Last_name
        self.age=age
        self.Regno=Regno
        self.course=course
    def __str__(self):
        return f"I am a student of {self.course} and my name is {self.First_name} {self.Last_name} and my age is {self.age} and my Regno is {self.Regno}"
    
# Child class1  
class Teacher(Student):
    def __init__(self,First_name,Last_name,age,Regno,course,subject):
        super().__init__(First_name,Last_name,age,Regno,course)
        self.subject=subject
    def __str__(self):
        return f"I am a teacher of {self.subject} and my name is {self.First_name} {self.Last_name} and my age is {self.age} and my Regno is {self.Regno}"
# Child class2   
class Principal(Teacher):
    def __init__(self,First_name,Last_name,age,Regno,course,subject,department):
        super().__init__(First_name,Last_name,age,Regno,course,subject)
        self.department=department
    def __str__(self):
        return f"I am a principal of {self.department} and my name is {self.First_name} {self.Last_name} and my age is {self.age} and my Regno is {self.Regno}"
    
    
def main():
    student1=Student("John","Doe",20,123,"Bsc")
    student2=Student("Jane","Doe",20,124,"Bsc")
    student3=Student("Jack","Doe",24,125,"Bsit")
    teacher1=Teacher("Kamau","Kamau",30,126,"Bsc","Maths")
    principal=Principal("prinasa","Mukasa",40,127,"Bsc","Maths","Maths")
    print(student1)
    print(student2)
    print(principal)
main()



