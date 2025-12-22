menu ={
    'momo':120,
    'pizza':360,
    'salad':200,
    'spring roll':180,
    'burger':240,
    'softdrink':100,

}

print("Welcome to spree restaurant")
print("momo:rs 120\npizza:rs 360\nsalad:rs200\nspring roll:rs180\nburger:rs240\nsoftdrink:rs100")
order_total=0
item_1=input("enter the name of dish you want to order=")
if item_1 in menu:
    order_total+= menu[item_1]
    print(f'Your order {item_1} has been added.')
    
else:
    print("the item is not in the menu would you like to order smthng else?")
another_order=input('do you want to add another order(yes/no)?')    
if another_order=='yes':
  item_2=input("enter the name of your second dish=")
if item_2 in menu:
    order_total+=menu [item_2]
    print(f"your order {item_2} has been placed")
    
else:
    print("kindly place another order")
print(f"the total amount you have to pay is {order_total}")