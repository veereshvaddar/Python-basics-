balance = 20000
pin = "1234"
p = input("enter your pin:")
if p == pin:
  amount= int(input(enter your amount to withdraw:"))
       if balance <= balance:
          balance = balance - amount 
          print("transaction successfull")
          print("remaning balance:",balance)
      else: 
          print("insufficient blance")
else: 
    print("incorrect pin")
    
