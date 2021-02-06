
try: 
    while True: 
        pattern = list(input())
        n = int(input())
        x = input().split()
        for i in range(len(x)):
            x[i] = int(x[i])
        msg = ''
        for i in range(len(x)):
            msg = msg+str(pattern[x[i]-1])
        print(msg)
except EOFError: 
    pass 