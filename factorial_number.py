# using for loop

num=int(input("enter the number--"))

fact=1

if num<0:
    print("factroial of 0 doesn't exist")
if num==0:
    print("factorial of 0 is 1")
if num>0:
    for i in range (1, num+1):
        fact=fact*i
    print("the factorial of given number is--",fact)


