class Student:
    def __init__(self):
        print("Welcome to No Args Constructor")
 
    def __init__(self, firstname):
        print("first Name :",firstname)
 
    def __init__(self, firstname,coursename,age):
        print("First Name :",firstname)
        print("Course Name :",coursename)
        print("Age :",age)
 
obj1=Student()
obj2=Student("Santosh")
obj3=Student("Santosh","Research and Science",22)
 
#Note: the above program provides Error Message, In Python We can not write more than one constructor in a same class.
#Note: Based on the above Program , Constructor overloading can not achieve in python.