
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

class ATM1:
    def __init__(self):
        self.pin=""
        self.balance=0

    def menu(self):
        print("Enter 1 For Set Pin")
        print("Enter 2 for Check Balance")
        print("Enter 3 for Withdraw Amount")
        print("Enter 4 for Deposite MOney")
        print("Enter 5 For Chnge Pin")
        print("Enter 6 for Exit")

        self.Choice=int(input("Enter Choice Here:"))

        match self.Choice:
            case 1:
                self.set_pin()
                

            case 2:
                self.check_balence()
                
            case 3:
                self.withdraw_amt()
               
  
            case 4:
                self.deposite_money()
                
            case 5:
                self.change_pin()
                
            case 6:
                self.exit()
                

    def set_pin(self):
        New_pin=input("please Set The Pin First")
        self.pin=New_pin
        print("Your PIN is:",self.pin)
        self.menu()

    def check_balence(self):
        pin=input("please enter pin first To check Balance")
        if self.pin==pin:
            print("Your Balance is:",self.balance)
        else:
            print("please give coorect pin")
        self.menu()

    def withdraw_amt(self):
        pin=input("please enter pin to done withdraw")
        if self.pin==pin:
            withdraw=int(input("Enter Amount To withdraw"))
            if self.balance>=withdraw:
                self.balance-=withdraw
                print("Your Current Balance is:",self.balance)
            else:
                print("Insuficeint Balance")
        else:
             print("please give corrrect pin")

        self.menu()

    def deposite_money(self):
        pin=input("please Enter pin first to deposite money")
        if self.pin==pin:
            depo=int(input("Enter Amount To Deposite"))
            self.balance += depo
            print("Your Current Balance is:",self.balance)
        else:
            print("incoorect pin")
        self.menu()

    def change_pin(self):
        pin=input("Please Enter current Pin:")
        if self.pin == pin:
            new_pin=input("please Enter New Pin")
            self.pin=new_pin
            print("your new pin is:",self.pin)
        else:
            print("incorrect pin")
        self.menu()

    def exit(self):
        print("Thank YOu")


obj1=ATM1()
obj1.menu()