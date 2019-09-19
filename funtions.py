#def student_score(name="khan",score=100):
#    print (name,"scored", score , "Marks")
#print(student_score(100))

def student_score(name,*score):
    print (name)
    print (score)

print(student_score("maya",75,55,80))

