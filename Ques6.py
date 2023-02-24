#6. Write a python script to create a Calculator 2.0 class with 2 methods for multiplication and division of 2 values 
#    and inherit it from the Calculator class.?
class calculater_2:
    def Multiply(self,number1,number2):
        print("Multiply :",number1*number2)

    def Division(self,number1,number2):
        if number2==0:
            print("ValueError! can not divide by Zero")
        else:
            print(number1/number2)
class calculater(calculater_2):
    def Adding(self,number1,number2):
        print("Addition :",number1+number2)

    def Subtraction(self,number1,number2):
        print("Subtraction:",number1-number2)

result=calculater()
result.Adding(30,2)
result.Multiply(25,2)
result.Division(60,0)

