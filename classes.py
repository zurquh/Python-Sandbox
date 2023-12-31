# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

#Create class 
class User:
    #Constructor 
    def _init_(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
    
    def greeting(self):
        return f'My name is {self.name} and i am {self.age} and my balance is {self.balance}'
    
    def has_birthday(self):
        self.age += 1 


#Extand class
class Customor(User):
 #Constructor 
    def _init_(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0
    
    def set_balance(self, balance):
        self.balance = balance


# Init user object 
brad = User('Brad Traversy', 'brad@gmail.com', 37)
#Init customer object 
janet = Customor('Janet Johnson', 'janet@yahoo.com', 25)

janet.set_balance(500)
print(janet.greeting())

brad.has_birthday()
print(brad.greeting())