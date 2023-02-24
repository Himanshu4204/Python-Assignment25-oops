#10. Write a python script to add the new method in SmartPhone class which accept 
#    Truecaller object as a parameter and call the fetch method of Truecaller.
class Truecaller:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, number):
        self.contacts[number]=name
        print("contact Added!")

    def fetch_number(self, number):
        if number in self.contacts:
            print(f"The name for {number} is {self.contacts[number]}")
        else:
            print(f"No contact found for number {number}")

class SmartPhone(Truecaller):
    def smart_phone(self):
        print("Video Calling")
        print("Gaming")

    def new_method(Truecaller):
        result.fetch_number(int(input("Enter a Number to Check in Truecaller :")))

result=Truecaller()
result.add_contact(input("Enter Name:"),int(input("Enter number:")))

phone_result=SmartPhone()
phone_result.new_method()

    



