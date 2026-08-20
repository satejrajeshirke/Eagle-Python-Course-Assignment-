"""
choose the options there 
ATM Process 
1.Enter 1 for Set Pin
2.Enter 2 for the Check Balance
3.Enter 3 for the Withdraw Ammount
4.Enter 4 for Deposite Ammount
5.Enter 5 for Chnage Pin
6.Enter 6 for Exit
"""

class ATM:
    def __init__(self):
        self.pin = " "
        self.balance = 0
        

    def menu(self):
        print("ATM Process")
        print("1.Enter 1 for Set Pin")
        print("2.Enter 2 for the Check Balance")
        print("3.Enter 3 for the Withdraw Ammount")
        print("4.Enter 4 for Deposite Ammount")
        print("5.Enter 5 for Chnage Pin")
        print("6.Enter 6 for Exit")

        self.choice=int(input("Enter Your Choise"))

        match self.choice:
            case 1:
                self.setpin()
                print("Your Pin is Setted sucessfully",self.pin)
                self.menu()
         
            case 2:
                self.check_balance()
                
         
            case 3:
                self.withdraw_amt()
         
            case 4:
                self.deposite_amt()
         
            case 5:
                self.change_pin()

            case 6:
                self.exit()    

            case _:
                print("Invalid Input")


    def setpin(self):
        if self.pin == " ":
            new_pin=input("Enter Pin First")
            self.pin=new_pin
        else:
            print("Pin is Already Set")

    def check_balance(self):
        pin=input("please Enter Pin First")
        if self.pin == pin:
            print("Your Account Balance is",self.balance) 
        else:
            print("please Enter Correct Pin")

        self.menu()
        

    def withdraw_amt(self):
        pin=input("Please Enter Pin Firt")
        if self.pin == pin:
            withdraw=int(input("Enter Amount For Withdraw"))
            if self.balance >= withdraw:
                self.balance= self.balance-withdraw
                print("Your Bank Balnce is:",self.balance)

        self.menu()
    
    def deposite_amt(self):
        depo =int(input("please Enter amount to deposite:"))
        self.balance = self.balance + depo

        print("Current Balence:",self.balance)
        self.menu()

    def change_pin(self):
        old_pin=input("Please Enter Old Pin First",)
        if self.pin == old_pin:
            new_pin=input("Enter New Pin")
            self.pin=new_pin
            print("new pin is:",self.pin)

        self.menu()

    def exit(self):
        print("Thank you")

            
obj1=ATM()
obj1.menu()