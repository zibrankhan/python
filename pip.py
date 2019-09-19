for i in range(0, 5):
    print(i+1),
    for j in range(5,i,-1):
        print("* "),
    print

#######################

for i in range(5):
        print("*" * (i+1))




#########

for i in range(5):
        print(" "*(5-i-1) + "*"*(2*i+1))
#################

for i in reversed(range(5)):
        print(" "*(5-i-1) + "*"*(2*i+1))