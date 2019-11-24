

num = input('Enter a number: ')
lis = list(num)
lis_length = len(lis)
a = 0
for i in lis:
    a += int(i) ** lis_length
if a == int(num):
    print(int(num),' is Armstrong number')
else:
    print(int(num),' is not Armstrong number')