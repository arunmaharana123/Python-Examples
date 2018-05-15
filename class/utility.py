# -*- coding: utf-8 -*-
class Banking:
    my_balance = 1000
    my_number = 0000
    my_pin = 0000

    def check_account(self, account_number, pin):
        self.my_number = account_number
        self.my_pin = pin
        return True

    def check_balance(self):
        print "\nAvailable Balance : Rs.", self.my_balance

    def withdraw_balance(self, amount):
        if self.my_balance >= amount:
            self.my_balance = self.my_balance - amount
            print "\nWithdraw Successfully !!!"
            print "\nRemaining Balance : Rs.",self.my_balance
        else:
            print "\nSORRY!!! You don't have sufficient balance to withdraw.\n"

    def add_balance(self, amount):
        self.my_balance = self.my_balance + amount
        print "\n%r added succefully to your account number -%r" %(amount, self.my_number)
        print "\nAvailable Balance :", self.my_balance

object = Banking()
status = object.check_account(310, 120)
if status == True:
    print "\nEnter\n 1: Check Balance \n 2: Withdraw Balance \n 3: Add Balance "
    key = raw_input("> ")
    if key == "1":
        object.check_balance()
    elif key == "2":
        amount = int(raw_input("\nEnter Amount : Rs. "))
        object.withdraw_balance(amount)
    elif key == "3":
        amount = int(raw_input("\nEnter Amount : Rs. "))
        object.add_balance(amount)
    else:
        print "\nYou entered a wrong keyword !!!!!! Thank You.\n"
