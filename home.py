x = 'java homw twecgnlogi'.split()
print(x)

a=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=int(input("Enter element:"))
    a.append(b)
a.sort()
print(a)
print("Second largest element is:",a[n-2])

## Reverse of a string

def reverse(s):
    str = ""
    for i in s:
        str = i + str  # appending chars in reverse order
    return str
s = "My Name Is Khan"
#print ("The reversed string(using loops) is : ",end="")
print (reverse(s))

# Program 2 print Fizz, Fuzz

for num in range(1, 21):
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)

# Sum & product of a given string

links=[1,2,3,4,5,6,7,8]
sum = 0
prod = 1
for i in links:
    sum = sum + i
    prod = prod *i
print('The sum of list is :'+ str(sum)  )
print('The product of list is :' + str(prod) )



# Reverse of a string
txt = "Hello World"[::-1]
print(txt)

# program for odd and even number

num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")

stry = "My name is khan"
count = 0

# occurance of a character

for i in stry:
    if i == 'a':
        count = count + 1
print("Count of a in My name is khan is : "
      + str(count))

te = "GeeksforGeeks"
counter = te.count('e')
print(counter)

# Program for writing 3 names with grade by taking input from user

name = []
grade = []
for i in range(3):
    input1 = input("Enter your Name")
    name.append(input1)
    input2 = input1("Enter your grade")
    grade.append(input2)
for i in range(0,3):
    print(i+1,"/t",name[i])