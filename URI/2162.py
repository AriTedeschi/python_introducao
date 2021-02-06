n = int(input())
x = input().split()
tipo = 'v'
check = 1

for i in range(len(x)):
    x[i] = int(x[i])

for i in range(n-1):
    if x[i] < x[i+1]:
        if i > 0 and tipo == 'v':
            check = 0
            break
        else:
            tipo='v'
    elif x[i] > x[i+1]:
        if i > 0 and tipo == 'p':
            check = 0
            break
        else:
            tipo='p'
    else:
        check = 0
        break

print(check)