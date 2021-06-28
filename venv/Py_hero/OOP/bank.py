print("This is a Apna bank")
class bank:
    def __init__(self,account,name,amount):
        self.account=account
        self.name=name
        self.amount=amount
    def print_bal(self):
        print(f"Hello..! \'{self.name}\'  your \'{self.account}\' acount balance is \'{self.amount}\' INR")
    def diposit(self,des):
        self.des=des
        print(f" Hello \"{self.name}\" you have deposite \"{self.des}\" INR amount")
        self.amount=self.amount+self.des
        print(f"\n\t {self.name} Now you account balance is {self.amount}")
    def withdraw_amt(self,diducted):
        self.diducted=diducted
        print(f"\nHello {self.name} You have withdraw this {self.diducted} INR amount")
        self.amount=self.amount-self.diducted
        print(f"\n\t\tNow you account balance is :{self.amount} INR")
type=input("Account Type ?: ")
name=input("Enter name:")
amt=int(input("Enter Amount:"))
obj= bank(type,name, amt)
obj.print_bal()
ds=int(input("You Can Deposite amount:"))
obj.diposit(ds)
amt=int(input("\n\tif wana withdraw enter :"))
obj.withdraw_amt(amt)