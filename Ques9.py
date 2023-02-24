#9. Write a python script to create an application like Truecaller where names and numbers are stored.
# Truecaller class will have 2 methods (1st to fetch the name of a number and 2nd to add a new entry).?
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

result=Truecaller()
result.add_contact(input("Enter Name:"),int(input("Enter number:")))
result.add_contact(input("Enter Name:"),int(input("Enter number:")))
    
print()
result.fetch_number(int(input("Enter a Number to Check in Truecaller :")))
