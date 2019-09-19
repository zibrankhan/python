#for i in range(0,5):
#    for j in range(0,i):
#        print (i), #print number
#    # new line after each row to display pattern correctly
#    print


#n = int(input("Enter number of rows: "))
#n = 5
#for i in range(n, 0, -1):
#    print((n - i) * ' ' + i * '*')

n=int(input("Enter a number: "))
for i in range(0,n):
    for j in range(0,n):
        if(i==j):
            print("1" , " ")
        else:
            print("0", " "),
    print