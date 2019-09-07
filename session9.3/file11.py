highscores= [45,56,46,65,78,98]
for i,n in enumerate(highscores):
    print(i,".",n)
a=int(input("enteryournewscore:"))
highscores.append(a)
for i,n in enumerate(highscores):
    print(i,".",n)
newlist=highscores.sort()
print(newlist)
print(1,".",highscores[6])
print(2,".",highscores[5])
print(3,".",highscores[4])
print(4,".",highscores[3])
print(5,".",highscores[2])
print(6,".",highscores[1])
print(7,".",highscores[0])



  