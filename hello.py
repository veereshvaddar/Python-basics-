num = int(input("Enter your number: "))
print(num)
def check_marks():
    marks = [20, 30, 50, 60, 45, 80]

    for i in marks:
        if i >= 50:
            print("Pass")
        else:
            print("Fail")

check_marks()
