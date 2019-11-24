import math
# 5! = 5*4*3*2*1

n = int(input('Enter a number: '))
#result = math.factorial(n)
#print('factorial of',n,'is',result)
result = 1
for i in range(1,n+1):
    result = result * i
print('factorial of',n,'is',result)