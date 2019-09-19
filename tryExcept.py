#value = 10/0

try:
    value = 10 / 0
    number = int(input("Enter the number"))
    print (number)

except ZeroDivisionError:
    print ("Divided by Zero")
except ValueError:
    print ("Invalid Input: ")

