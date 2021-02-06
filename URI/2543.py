
try: 
    while True: 
        n, i = input().split()
        cnt = 0
        for x in range(0,int(n)):
            a,t = input().split()
            
            if a == i and t == '0':
                cnt+=1
        print(cnt)
except EOFError: 
    pass 