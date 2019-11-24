
#An Armstrong number is a number such that the sum !
#of its digits raised to the third power is equal to the number ! itself
num = int(input('Enter a number: '))
list_arm = []
for z in range(0,num+1):
    z_str = str(z)
    lis_length = len(z_str)
    num_one = 0
    num_one += z ** lis_length
    if num_one == z:
        list_arm.append(z)
print('Armstrong numbers between 0 to',num,':',list_arm)