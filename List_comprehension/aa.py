l = ["abc", "abv", "qwe", "shs", "flhlf"]
l2 = []
#print("".join(list(reversed(st))))
#print(list(l2))
# for i in l:
#    if i == "".join(list(reversed(i))):
#        l2.append(i)
# print(l2)
for i in l:
   if i == i[::-1]:
       l2.append(i)
#print(l2)
abc = [var for var in l if var == var[::-1]]
print(abc)