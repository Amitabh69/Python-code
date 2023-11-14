#  ax **2 +bx +c=0
# a=b=c= real numbers
# a!=0

import cmath
a=int(input("enter for a--"))
b=int(input("enter for b--"))
c=int(input("enter for c--"))

# finding discriminants

d= (b**2)-(4*a*c)

# finding roots

root1=(-b-cmath.sqrt(d))/(2*a)
root2=(-b+cmath.sqrt(d))/(2*a)

print("root 1 is--",root1)
print("root 2 is--",root2)