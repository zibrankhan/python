num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
num3 = input("Enter third number: ")

if num1>num2 and num1>num3:
    print("first number is greater")

elif num2>num1 and num2>num3:
    print("second number is greter")

elif num1==num2 and num1==num3:
    print ("All are equal")
    
else:
    print("third number is greter")
