Choice=int(input("Enter your choice (1 for Addition, 2 for Subtraction, 3 for Multiplication, 4 for Division): "))
print("Enter two numbers:")
a ,b=map(int, input(" ").split())

if Choice==1:
    result=a+b
    print("The result of addition is:", result)
elif Choice==2:
    result=a-b
    print("The result of subtraction is:", result)
elif Choice==3:
    result=a*b
    print("The result of multiplication is:", result)
elif Choice==4:
    if b!=0:
        result=a/b
        print("The result of division is:", result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid choice. Please select a valid operation.")