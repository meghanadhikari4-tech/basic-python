class bank:
    def __init__(self,name,initial_balance):
        self.name=name
        self.__initial_balance=initial_balance
    def deposit(self,amount):
        self.__initial_balance=self.__initial_balance+amount#private property
    def withdraw(self,amount):
        self.__initial_balance=self.__initial_balance-amount
    def show_balance(self):
        print(f"your total balance is {self.__initial_balance}")

acc=bank("meghan",20000)
while True:
 print("\n your available options")
 print("1.deposit\n","2.withdraw\n","3.show_balance")
 choice=int(input("enter your choice:"))

 if choice==1:
     amount=int(input("enter the amount you want to deposit"))
     acc.deposit(amount)
     print(f"the amount you deposited is{amount}")

 elif choice==2:
    amount=int(input("enter the amount you want to withdraw"))
    acc.withdraw(amount)
    print(f"the amount you withdraw is {amount}")

 elif choice==3:
        acc.show_balance()

 else:
        print("invalid")
        
    