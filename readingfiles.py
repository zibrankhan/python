
# r is used to read
# w is used for write
# r+ used for read and write
# a is used for append at the end of file

family_file = open("text.txt", "r")
for family in family_file.readlines():
    print (family)
#print(family_file.readable())
#print (family_file.read())
#print (family_file.readline())
#print (family_file.readlines())



family_file.close()
