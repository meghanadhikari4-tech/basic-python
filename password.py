import random
import string

length=int(input("enter the length of the password:"))
letter=string.ascii_letters
digit=string.digits
symbols="@#$%&"
combine=letter+digit+symbols
password="".join(random.choice(combine)for _ in range(length))

print(f"your randome choice of password is{password}:")