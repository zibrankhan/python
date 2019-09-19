#x = input("Enter first number: ")
#y = input("Enter second number: ")
#z = input("Enter third number: ")

#print(max(x,y,z))

lists = [1,2,[3,4],5,6,7,8,9]
print(lists[4:8])
l1 = ["a","b","c","d","e"]
print (l1[2:3])
lists[2][1]=10
print (lists)

num = int(input("enter the number? "))
if num%2 == 0:
    print("Number is even...")
else:
    print("Number is odd...")

number = int(input("Enter the number?"))
if number==10:
    print("number is equals to 10")
elif number==50:
    print("number is equal to 50");
elif number==100:
    print("number is equal to 100");
else:
    print("number is not equal to 10, 50 or 100");