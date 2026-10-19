import re
a="2"
print(a.isalnum())
r=r"ab+\s+\w"
print(re.match(r,"f"))
print(re.match(r,"abbb  f"))



a=[1,2,3,4,5,6]
b="asdfghi"
c=(True, False, None,print,input)

l=min(len(a),len(b),len(c))
for i in range(l):
    print(a[i],b[i],c[i])


for i,j,k in zip(a,b,c):
    print(i,j,k)

print(zip(a,b,c))