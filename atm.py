
accounts={
   "meghan":{"pin":"1234","balance":2000000,"history":[]},
   "rani":{"pin":"2345","balance":123456789,"history":[]}
}
Max_withdraw=250000
min_withdraw=100
max_deposit=500000
min_deposit=100
while True:
   account=input("enter your account name(or exit to quit)")
   if account.lower()=="exit":
      print("thanlyou for using the atm")
      break
   if account not in accounts:
      print("account not found")
      continue
   attempt=3
    
   while attempt>0:
      entered_pin=input("enter your 4 digit pin: ")
      if entered_pin==accounts[account]["pin"]:
         print("login successfully")
         break
      else:
         attempt-=1
         print("please input  valid pin:")
   if attempt==0:
      print("you re logged out")
      continue
   while True:
    print("....ATM....")
    print("1.check amount")
    print("2.deposit money")
    print("3.withdraw amount")
    print("4.exit")
    choice=input("enter your choice (1:4)")
    if choice in["1","2","3","4"]:
       entered_pin=input("enter a four digit pin")
       if len(entered_pin)!=4 or not entered_pin.isdigit():
          print("please put a avlid lenght pin")
          continue
          
       if entered_pin !=accounts[account]['pin']:
          logged_in = False  
          print("please put valid pin")
          continue
       
    if choice=="1":
        print(f"your balance is {accounts [account]["balance"]}")
    elif choice=="2":
        amount=float(input("enter the amount you want to deposit"))
        accounts[account]["balance"]+=amount
        print(f"you deposited the amount{amount}")
    elif choice=="3":
        amount=float(input("enter the amount you want to withdraw"))
        if amount>accounts[account]["balance"]:
         print("sorry insufficient banlance")
        else:
         accounts[account]["balance"]-=amount
         print("you can withdraw the cash")
    elif choice=="4":
       print("thankyou for using ATM machine")
    else:
       print("invalid choice")
