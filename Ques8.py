#8. Write a python script to create a SmartPhone class by inheriting Calculator 2.0 and Phone Class.?
class calculater_20:
    def multiply(self,number1,number2):
        print("Multiplication :",number1*number2)

    def Division(self,number1,number2):
        if number2==0:
            print("ValueError! can not Divide by Zero")
        else:
            print('Division :',number1/number2)
class Normal_phone:

    def normal_phone(self):
        print("Calling")
        print("SMS")
    
class SmartPhone(Normal_phone,calculater_20):
    def smart_phone(self):
        print("Video Calling")
        print("Gaming")

result=SmartPhone()
result.normal_phone()
result.Division(12,6)
result.smart_phone()

