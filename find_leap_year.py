num=int(input("enter the year--"))

if (num % 400 == 0) and (num % 100 == 0):
    print(num,"is a leap year")

elif (num % 4 == 0) and (num % 100 !=0):
    print(num, "is a leap year")

else:
    print(num, "isn't a leap year")