values = input().split()
for x in range(0,3):
    values[x] = int(values[x])
for x in sorted(values):
    print(x)
print('')

for x in values:
    print(x)