def grades():
    marks = int(input("Enter your marks:"))

    if marks >= 90:
        print("A Grade")
    elif marks >= 75:
        print("B Grade")
    elif marks >= 50:
        print("C Grade")
    else:
        print("Fail")

grades()
