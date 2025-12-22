class user:
    def __init__(self,name,membership):
        self.name=name
        self.membership=membership
    def apply_discount(self,total):
        return

class regularuser(user):
    def apply_discount(self,total):
        return total


class premiumuser(user):
    def apply_discount(self,total):
        return total*0.90
    
class shoppingcart():
    def __init__(self):
        self.items=[]
    def add_items(self,price):
        self.items.append(price)

    def get_total(self):
        return sum(self.items)

    def checkout(self, user):
        total = self.get_total()
        return user.apply_discount(total)
cart =shoppingcart()
cart.add_items(100)
cart.add_items(200)

user1 = premiumuser("Meghan", "premium")
print(cart.checkout(user1))
    