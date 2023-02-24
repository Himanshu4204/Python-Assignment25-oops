#3. Write a python script to update 2nd Question, change email and age to __email and __age.?
class Profile:
    def __init__(self):
        self.__name="Himanshu"
        self.__email=None  
        self.__age=None

    def update_profile(self):
        self.__email=input("Enter your Email:")
        self.__age=input("Enter your Age:")

    def get_profile(self):
        print()           
        print("Name:",self.__name)
        print("Email:",self.__email)
        print("Age:",self.__age)
    
Obj=Profile()
Obj.update_profile()
Obj.get_profile()
