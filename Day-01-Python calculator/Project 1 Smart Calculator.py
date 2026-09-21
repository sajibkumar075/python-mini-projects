Choice=int(input("Enter your choice (1 for Addition, 2 for Subtraction, 3 for Multiplication, 4 for Division): "))
print("Enter two numbers:")
a ,b=input(" ").split()

if Choice==1:
    result=int(a)+int(b)
    print("The result of addition is:", result)
elif Choice==2:
    result=int(a)-int(b)
    print("The result of subtraction is:", result)
elif Choice==3:
    result=int(a)*int(b)
    print("The result of multiplication is:", result)
elif Choice==4:
    result=int(a)/int(b)
    print("The result of division is:", result)