balance = 5000
pin = "1234"

p = input("Enter your PIN: ")

if p == pin:
    print("Login Successful")
    print("Balance:", balance)
else:
    print("Invalid PIN")
