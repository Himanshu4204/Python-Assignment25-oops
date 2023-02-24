#1. Write a python script to create a Profile class with 3 attributes (name, email, age).?
class Profile:
    def __init__(self,name,email,age):
        self.name=name
        self.email=email
        self.age=age
    
    def show_profile(self):
        print(f"Name:{Obj.name}\n Email:{Obj.email}\n Age:{Obj.age}")

Obj=Profile("Himanshu","abc@gmail.com",20)
Obj.show_profile()
