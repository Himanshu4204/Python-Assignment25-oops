#4. Write a python script to update 2nd Question, add a class variable (platform) and create a classmethod to access it.?
class Profile:
    platform="Ineuron"

    def __intit__(self,name,email,age):
        self.__name=None
        self.__email=None
        self.__age=None

    def set_profile(self):
        self.__name=input("Enter your Name :")
        self.__email=input("Enter your email :")
        self.__age=input("Enter your age :")

    def get_Platform(self):
        print("Platform:",Profile.platform)

    def get_profile(self):
        print("Name :",self.__name)
        print("Email :",self.__email)
        print("Age :",self.__age)

Obj=Profile()
Obj.set_profile()
Obj.get_Platform()
Obj.get_profile()

