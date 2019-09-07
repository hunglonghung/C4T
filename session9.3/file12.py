highscores= [45,56,46,65,78,98]
abc=highscores.sort()
print(abc)
print(1,".",highscores[5])
print(2,".",highscores[4])
print(3,".",highscores[3])
print(4,".",highscores[2])
print(5,".",highscores[1])

a=int(input("enteryournewscore:"))
highscores.append(a)

newlist=highscores.sort()
print(newlist)
print(1,".",highscores[6])
print(2,".",highscores[5])
print(3,".",highscores[4])
print(4,".",highscores[3])
print(5,".",highscores[2])



b=int(input("enteryournewscore:"))
highscores.append(b)

new=highscores.sort()
print(new)
print(1,".",highscores[7])
print(2,".",highscores[6])
print(3,".",highscores[5])
print(4,".",highscores[4])
print(5,".",highscores[3])
