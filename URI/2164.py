import math
n = int(input())
#Fibonacci

r  = math.pow(( 1 + math.sqrt(5) ) / 2, n)
r -= math.pow(( 1 - math.sqrt(5) ) / 2, n)
r /= math.sqrt(5)
print('{:.1f}'.format(r))