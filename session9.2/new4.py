like= ["anime","manga","light novel"]
l=input("additional favourite:")
like.append(l)

m=input("additional favourite:")
like.append(m)
n=input('addiotional favourite:')
like.append(n)

print(*like, sep="," )
print(like[0])
print(like [1])
print(like[2])
print(like[-1])
print(like[-2])
