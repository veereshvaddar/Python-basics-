balance = 10000
pin = "1234"
p = input(enter your pin:")
if p == pin:
  amount = int(input("enter your amount to deposit:"))
     balance = balance + amount
     print("deposite successfully")
     print("remaining balance:",balance)
else: 
     print("incorrect pin")
