n = 10
print('n = ', n)
for i in range(n+1):
    
    print('\t'*(n-i), end='')
    
    for j in range(i):
        print('X',  end='\t\t')
    print()