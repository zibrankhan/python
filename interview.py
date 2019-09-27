mylist=[0,1,2,3,4,5,6,7,8,9]
print(mylist[1:5])
print(mylist[::-1])
mylist.append(4)
print(mylist)
mylist1=[0,1,2,[3,4,5,8],6,7,8,9]
mylist1[3][3]=1
print(mylist1)
a,b=10,20
a,b=b,a
print(a,b)

num = int(input("Enter a number: "))
sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")


for i in range(5,0,-1):
    print('')