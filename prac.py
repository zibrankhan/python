#for i in range (0,5):
#    for j in range(0,i+1):
#        print("*",end=""),
#    print()
#my_dict={'id':101,'name':('khan','ayan','aadil')}
#print(my_dict)
#print(my_dict.keys())
#print(my_dict.values())

#class Parrot:

    # class attribute
 #   species = "bird"

    # instance attribute
   # def __init__(self, name, age):
 #       self.name = name
   #     self.age = age
# instantiate the Parrot class
#blu = Parrot("Blu", 10)
#woo = Parrot("Woo", 15)

class student:
    def __init__(self,rollno,name):
        self.rollno=rollno
        self.name=name
    def talk(self):
        print('Hello My Name Is',self.name)
        print('My Rollno is ',self.rollno)

s = student(100,'king')
print(s.rollno)
print(s.name)
s.talk()
s1=student(200,'ayan')
s.talk()