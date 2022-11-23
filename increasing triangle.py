n=10
for k in range(n):
    for i in range(k,n):
        print(' ', end=' ')
    for i in range(k + 1):
        print('*', end=' ')
    print()
