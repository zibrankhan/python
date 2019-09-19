numb = [18,4,9,3,7,2]
friend=["allen","kolaar","kiran","lilliput", 45]
friend[1]= "star"
print (friend)
print(friend[0][::-1], friend[1][::-1], friend[2][::-1])
print (numb)
friend.append("tabbu")
friend.insert(2,"babu")
friend.remove(45)
friend.extend(numb)
print (friend)
print (friend.count("kiran"))
numb.reverse()
print (numb)
#friend2 = friend.copy()
#print (friend2)

