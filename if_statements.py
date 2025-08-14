marks=int(input("Enter the marks you got: "))

if marks>100 or marks<0:
    print("Invalid Input")

elif marks>=90:
    print("Grade=A")

elif marks>=80:
    print("Grade=B")

elif marks>=70:
    print("Grade=C")

elif marks>=60:
    print("Grade=D")


else:
    print("Fail")