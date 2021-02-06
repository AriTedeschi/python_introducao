s = 1
l = list()
while s > 0:
    s = float(input())
    if s > 0:
        l.append(s)

print('{:.2f}'.format(sum(l)/len(l)))