n = int(input('enter a anumber: '))

#  1
#  12
#  123
#  1234
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()

#  1
#  22
#  333
#  4444
#for i in range(1,n+1):
#    for j in range(1,i+1):
#        print(i,end='')
#    print()