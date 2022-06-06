# OOPS in Python 

#  INHERITANCE IN OOP'S USING PYTHON
#  CREATING A BASE CLASS

class Animal():
    def __init__(self):
        print("Animal base class created ")
     

    def who_am_i(self):
        print("I am a Animal ")
        
        
        
        
        
# Created a Derived Class called Dog

class Dog(Animal):
    
    def __init__(self):
        Animal.__init__(self)
        print("Derived Class Dog Created ")
        
    def who_am_i(self):
        print('I am Dog')
        
    def bark(self):
        print("WOOF!")
        
        
mydog = Dog()

mydog.bark()       

mydog.who_am_i()
        

