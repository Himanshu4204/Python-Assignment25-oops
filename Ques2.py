#2. Write a python script to update the above Profile class with encapsulation.?
class Profile:
    def __init__(self):
        self.__name="Himanshu"
        self.__email="himanshurajput14504@gmail.com"   
        self.__age=20

    def update_profile(self):
        self._name=input("Enter your Name :")
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
